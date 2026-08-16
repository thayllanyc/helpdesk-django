from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ("username", "email", "papel", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        ("Informações do helpdesk", {"fields": ("papel",)}),
    )