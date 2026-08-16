from django.conf import settings
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Chamado(models.Model):
    class Status(models.TextChoices):
        ABERTO = "ABERTO", "Aberto"
        EM_ANDAMENTO = "EM_ANDAMENTO", "Em andamento"
        RESOLVIDO = "RESOLVIDO", "Resolvido"
        FECHADO = "FECHADO", "Fechado"
    class Chamado(models.Model):
    # ... todos os campos que já existem, sem mudar nada ...

     def __str__(self):
        return f"#{self.pk} - {self.titulo}"

    class Meta:
        ordering = ["-criado_em"]

    class Prioridade(models.TextChoices):
        BAIXA = "BAIXA", "Baixa"
        MEDIA = "MEDIA", "Média"
        ALTA = "ALTA", "Alta"

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.ABERTO
    )
    prioridade = models.CharField(
        max_length=10, choices=Prioridade.choices, default=Prioridade.MEDIA
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="chamados"
    )
    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chamados_abertos",
    )
    agente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="chamados_atribuidos",
        null=True,
        blank=True,
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.pk} - {self.titulo}"

class Comentario(models.Model):
    chamado = models.ForeignKey(
        Chamado, on_delete=models.CASCADE, related_name="comentarios"
    )
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comentarios"
    )
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor} em #{self.chamado_id}"

    class Meta:
        ordering = ["criado_em"]