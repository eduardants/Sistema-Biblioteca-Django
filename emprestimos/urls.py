from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_emprestimos, name='listar_emprestimos'),
    path('devolver/<int:id>/', views.devolver_emprestimo, name='devolver_emprestimo'),
    path('excluir/<int:id>/', views.excluir_emprestimo, name='excluir_emprestimo'),
]