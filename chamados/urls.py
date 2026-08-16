from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="chamados/login.html"), name="login"),
    path("", views.lista_chamados, name="lista_chamados"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("novo/", views.criar_chamado, name="criar_chamado"),
    path("<int:chamado_id>/", views.detalhe_chamado, name="detalhe_chamado"),
    path("<int:chamado_id>/gerenciar/", views.gerenciar_chamado, name="gerenciar_chamado"),
    path("<int:chamado_id>/comentar/", views.adicionar_comentario, name="adicionar_comentario"),
]