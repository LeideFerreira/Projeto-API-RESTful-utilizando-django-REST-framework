from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacao
from endereco.models import Endereco


# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)  # relacao muitos para muitos
    comentarios = models.ManyToManyField(Comentarios)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ManyToManyField(Endereco)

    def __str__(self):
        return self.nome
