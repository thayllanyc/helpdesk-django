from django.test import TestCase
from django.urls import reverse
from contas.models import Usuario
from .models import Categoria, Chamado


class ListaChamadosTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Suporte")

        self.cliente1 = Usuario.objects.create_user(
            username="cliente1", password="senha123", papel=Usuario.Papel.CLIENTE
        )
        self.cliente2 = Usuario.objects.create_user(
            username="cliente2", password="senha123", papel=Usuario.Papel.CLIENTE
        )

        self.chamado1 = Chamado.objects.create(
            titulo="Chamado do cliente 1",
            descricao="teste",
            categoria=self.categoria,
            cliente=self.cliente1,
        )
        self.chamado2 = Chamado.objects.create(
            titulo="Chamado do cliente 2",
            descricao="teste",
            categoria=self.categoria,
            cliente=self.cliente2,
        )

    def test_cliente_ve_apenas_proprio_chamado(self):
        self.client.login(username="cliente1", password="senha123")
        response = self.client.get(reverse("lista_chamados"))

        self.assertContains(response, "Chamado do cliente 1")
        self.assertNotContains(response, "Chamado do cliente 2")

    def test_usuario_nao_logado_e_redirecionado(self):
        response = self.client.get(reverse("lista_chamados"))
        self.assertEqual(response.status_code, 302)

    def test_admin_ve_todos_os_chamados(self):
        admin = Usuario.objects.create_user(
            username="admin_teste", password="senha123", papel=Usuario.Papel.ADMIN
        )
        self.client.login(username="admin_teste", password="senha123")
        response = self.client.get(reverse("lista_chamados"))

        self.assertContains(response, "Chamado do cliente 1")
        self.assertContains(response, "Chamado do cliente 2")