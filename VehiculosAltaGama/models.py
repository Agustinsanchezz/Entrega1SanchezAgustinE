from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Sedan(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    anio = models.IntegerField()
    precio = models.IntegerField()
    
    
class Camioneta(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    anio = models.IntegerField()
    precio = models.IntegerField()
    
    
    
    
class Deportivo(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    anio = models.IntegerField()
    precio = models.IntegerField()
            