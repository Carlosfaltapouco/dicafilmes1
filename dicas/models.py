from email.policy import default
from pickle import TRUE
from turtle import mode
from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class Dica(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_dica = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    onde_assistir = models.CharField(max_length=200)
    nota_de_avaliacao = models.CharField(max_length=200)
    comentarios = models.TextField()
    date_da_dica = models.DateField(default=datetime.now, blank=True)
    foto_dica = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    publicada = models.BooleanField(default=False)