from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario


def listar_usuarios(request):
    todos_usuarios = Usuario.objects.all().order_by('nome')

    return render(
        request,
        'usuarios/listar_usuarios.html',
        {'usuarios': todos_usuarios}
    )


def desativar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.desativar()

    return redirect('listar_usuarios')


def ativar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.ativar()

    return redirect('listar_usuarios')