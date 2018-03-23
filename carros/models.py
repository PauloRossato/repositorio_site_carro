# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models




class Fabricante(models.Model):
    nome = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.nome





# Create your models here.
class Carro(models.Model):
    name = models.CharField(max_length=300)
    valor = models.FloatField(10000)
    ano = models.IntegerField(10000)
    modelo = models.CharField(max_length=300)
    fabricante = models.ForeignKey(Fabricante, null=True)

    def __str__(self):
        return self.name