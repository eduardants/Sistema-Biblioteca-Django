from django.contrib import admin
from .models import Emprestimo


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = (
        'livro',
        'usuario',
        'data_retirada',
        'data_devolucao',
        'status',
    )

    search_fields = (
        'livro',
        'usuario',
    )

    list_filter = (
        'status',
        'data_retirada',
        'data_devolucao',
    )

    ordering = ('-data_retirada',)