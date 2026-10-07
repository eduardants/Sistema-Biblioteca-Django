from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from emprestimos.models import Emprestimo


def listar_livros(request):

    todos_livros = Livro.objects.all().order_by('titulo')

    return render(
        request,
        'livros/listar_livros.html',
        {'livros': todos_livros}
    )


def retirar_livro(request, id):

    livro = get_object_or_404(Livro, id=id)

    # Verifica se ainda existem exemplares disponíveis
    if livro.disponivel <= 0:

        return render(
            request,
            'livros/listar_livros.html',
            {
                'livros': Livro.objects.all().order_by('titulo'),
                'erro': 'Não há exemplares disponíveis deste livro.'
            }
        )

    # Cria o empréstimo
    Emprestimo.objects.create(
        livro=livro,
        usuario='Não informado'
    )

    return redirect('listar_livros')


def devolver_livro(request, id):

    livro = get_object_or_404(Livro, id=id)

    # Procura um empréstimo ativo desse livro
    emprestimo = Emprestimo.objects.filter(
        livro=livro,
        status='emprestado'
    ).first()

    if emprestimo:

        emprestimo.devolver()

    return redirect('listar_livros')
