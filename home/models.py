from django.db import models


class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensagem de {self.nome} ({self.email})'


