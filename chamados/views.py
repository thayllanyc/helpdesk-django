from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import HttpResponseForbidden
from .models import Chamado
from .forms import ChamadoForm, GerenciarChamadoForm, ComentarioForm
from contas.models import Usuario
from django.core.paginator import Paginator

@login_required
def lista_chamados(request):
    usuario = request.user

    if usuario.papel == Usuario.Papel.ADMIN:
        chamados = Chamado.objects.all()
    elif usuario.papel == Usuario.Papel.AGENTE:
        chamados = Chamado.objects.filter(
            Q(cliente=usuario) | Q(agente=usuario)
        )
    else:
        chamados = Chamado.objects.filter(cliente=usuario)

    status_filtro = request.GET.get("status")
    if status_filtro:
        chamados = chamados.filter(status=status_filtro)

    busca = request.GET.get("busca")
    if busca:
        chamados = chamados.filter(titulo__icontains=busca)

    paginator = Paginator(chamados, 5)
    numero_pagina = request.GET.get("page")
    pagina = paginator.get_page(numero_pagina)

    return render(request, "chamados/lista_chamados.html", {"chamados": pagina})

@login_required
def detalhe_chamado(request, chamado_id):
    usuario = request.user

    if usuario.papel == Usuario.Papel.ADMIN:
        chamado = get_object_or_404(Chamado, id=chamado_id)
    elif usuario.papel == Usuario.Papel.AGENTE:
        chamado = get_object_or_404(
            Chamado, Q(cliente=usuario) | Q(agente=usuario), id=chamado_id
        )
    else:
        chamado = get_object_or_404(Chamado, id=chamado_id, cliente=usuario)

    form_comentario = ComentarioForm()

    return render(
        request,
        "chamados/detalhe_chamado.html",
        {"chamado": chamado, "form_comentario": form_comentario},
    )
        
@login_required
def criar_chamado(request):
    if request.method == "POST":
        form = ChamadoForm(request.POST)
        if form.is_valid():
            chamado = form.save(commit=False)
            chamado.cliente = request.user
            chamado.save()
            return redirect("detalhe_chamado", chamado_id=chamado.id)
    else:
        form = ChamadoForm()

    return render(request, "chamados/criar_chamado.html", {"form": form})


@login_required
def gerenciar_chamado(request, chamado_id):
    usuario = request.user

    if usuario.papel not in (Usuario.Papel.ADMIN, Usuario.Papel.AGENTE):
        return HttpResponseForbidden("Você não tem permissão para gerenciar chamados.")

    if usuario.papel == Usuario.Papel.ADMIN:
        chamado = get_object_or_404(Chamado, id=chamado_id)
    else:
        chamado = get_object_or_404(
            Chamado, Q(cliente=usuario) | Q(agente=usuario), id=chamado_id
        )

    if request.method == "POST":
        form = GerenciarChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            return redirect("detalhe_chamado", chamado_id=chamado.id)
    else:
        form = GerenciarChamadoForm(instance=chamado)

    return render(request, "chamados/gerenciar_chamado.html", {"form": form, "chamado": chamado})

@login_required
def adicionar_comentario(request, chamado_id):
    usuario = request.user

    if usuario.papel == Usuario.Papel.ADMIN:
        chamado = get_object_or_404(Chamado, id=chamado_id)
    elif usuario.papel == Usuario.Papel.AGENTE:
        chamado = get_object_or_404(
            Chamado, Q(cliente=usuario) | Q(agente=usuario), id=chamado_id
        )
    else:
        chamado = get_object_or_404(Chamado, id=chamado_id, cliente=usuario)

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.chamado = chamado
            comentario.autor = usuario
            comentario.save()

    return redirect("detalhe_chamado", chamado_id=chamado.id) 

@login_required
def dashboard(request):
    usuario = request.user

    if usuario.papel == Usuario.Papel.ADMIN:
        chamados = Chamado.objects.all()
    elif usuario.papel == Usuario.Papel.AGENTE:
        chamados = Chamado.objects.filter(
            Q(cliente=usuario) | Q(agente=usuario)
        )
    else:
        chamados = Chamado.objects.filter(cliente=usuario)

    contagem_por_status = {
        "ABERTO": chamados.filter(status="ABERTO").count(),
        "EM_ANDAMENTO": chamados.filter(status="EM_ANDAMENTO").count(),
        "RESOLVIDO": chamados.filter(status="RESOLVIDO").count(),
        "FECHADO": chamados.filter(status="FECHADO").count(),
    }

    return render(request, "chamados/dashboard.html", {"contagem": contagem_por_status})