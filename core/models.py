from django.db import models
from atracoes.models import Atracao


# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)  # relacao muitos para muitos

    def __str__(self):
        return self.nome