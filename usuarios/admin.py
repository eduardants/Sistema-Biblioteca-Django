from django.contrib import admin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'email',
        'telefone',
        'data_cadastro',
        'ativo',
    )

    search_fields = (
        'nome',
        'email',
        'telefone',
    )

    list_filter = (
        'ativo',
        'data_cadastro',
    )

    ordering = ('nome',)