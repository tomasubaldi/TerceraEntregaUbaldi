from django.db import models

class EquipoMusical(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    potencia = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)