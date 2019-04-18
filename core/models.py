from django.db import models
from atracoes.models import *
from comment_review.models import *
from avaliacoes.models import *
from enderecos.models import *

# Create your models here.
class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Atracao)
    comments = models.ManyToManyField(Comments)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.name