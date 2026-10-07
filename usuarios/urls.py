
from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),

    path(
        'desativar/<int:id>/',
        views.desativar_usuario,
        name='desativar_usuario'
    ),

    path(
        'ativar/<int:id>/',
        views.ativar_usuario,
        name='ativar_usuario'
    ),
]
