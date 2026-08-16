from django.contrib import admin
from .models import Categoria, Chamado


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")


@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "status", "prioridade", "cliente", "agente", "criado_em")
    list_filter = ("status", "prioridade", "categoria")
    search_fields = ("titulo", "descricao")