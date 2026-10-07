from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('retirar/<int:id>/', views.retirar_livro, name='retirar_livro'),
    path('devolver/<int:id>/', views.devolver_livro, name='devolver_livro'),
]