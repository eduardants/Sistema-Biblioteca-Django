from django.shortcuts import render, get_object_or_404, redirect
from .models import Emprestimo


def listar_emprestimos(request):
    todos_emprestimos = Emprestimo.objects.all().order_by('-data_retirada')

    return render(
        request,
        'emprestimos/listar.html',
        {'emprestimos': todos_emprestimos}
    )


def devolver_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.devolver()

    return redirect('listar_emprestimos')


def excluir_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.delete()

    return redirect('listar_emprestimos')