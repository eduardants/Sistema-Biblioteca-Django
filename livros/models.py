from django.db import models


class Livro(models.Model):

    titulo = models.CharField(max_length=100)

    autor = models.CharField(max_length=100)

    isbn = models.CharField(max_length=20, unique=True)

    ano_publicacao = models.IntegerField()

    quantidade_disponivel = models.IntegerField(default=0)

    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    @property
    def quantidade_emprestada(self):
        return self.emprestimos.filter(
            status='emprestado'
        ).count()

    @property
    def disponivel(self):
        return (
            self.quantidade_disponivel
            - self.quantidade_emprestada
        )

    @property
    def status_disponibilidade(self):
        if self.disponivel > 0:
            return "Disponível"

        return "Indisponível"
