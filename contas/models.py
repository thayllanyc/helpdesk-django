from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    class Papel(models.TextChoices):
        CLIENTE = "CLIENTE", "Cliente"
        AGENTE = "AGENTE", "Agente"
        ADMIN = "ADMIN", "Administrador"

    papel = models.CharField(
        max_length=10,
        choices=Papel.choices,
        default=Papel.CLIENTE,
    )

    def __str__(self):
        return self.username