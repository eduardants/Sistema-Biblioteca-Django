from django.contrib import admin
from .models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'autor',
        'isbn',
        'quantidade_disponivel',
        'ano_publicacao',
        'data_cadastro',
    )

    search_fields = (
        'titulo',
        'autor',
        'isbn',
    )

    list_filter = (
        'ano_publicacao',
        'data_cadastro',
    )

    ordering = ('titulo',)