from django.db import models
from datetime import date
from livros.models import Livro


class Emprestimo(models.Model):

    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name='emprestimos'
    )

    usuario = models.CharField(max_length=100)

    data_retirada = models.DateField(auto_now_add=True)

    data_devolucao = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ('emprestado', 'Emprestado'),
            ('devolvido', 'Devolvido'),
            ('atrasado', 'Atrasado'),
        ],
        default='emprestado'
    )

    observacao = models.TextField(blank=True)

    def esta_atrasado(self):

        if self.data_devolucao:
            return False

        return date.today() > self.data_retirada

    def devolver(self):

        self.data_devolucao = date.today()
        self.status = 'devolvido'

        self.save()

    def __str__(self):

        return f"{self.livro.titulo} - {self.usuario}"
