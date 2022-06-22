from django.db import models
from datetime import datetime

class Lista(models.Model):
    cep = models.IntegerField(blank=False)
    endereco = models.TextField(blank=False)
    complemento = models.TextField(max_length=50)
    bairro = models.TextField(blank=False)
    cidade = models.TextField(blank=False)
    uf = models.CharField(max_length=5, blank=False)
    numero = models.IntegerField(blank=False)
    descricao = models.TextField(max_length=100)
    data_adicionado = models.DateTimeField(default=datetime.now, blank=True)
    
