from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path('', index, name='index'),

    path('admin/', admin.site.urls),

    path('usuarios/', include('usuarios.urls')),

    path('livros/', include('livros.urls')),

    path('emprestimos/', include('emprestimos.urls')),
]
