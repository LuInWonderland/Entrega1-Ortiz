from django.db import models

# Create your models here.
class CienciaFiccion(models.Model):
    titulo = models.CharField(max_length=40)
    autor  = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=255)
    url_portada = models.CharField(max_length=40)

class Terror(models.Model):
    titulo = models.CharField(max_length=40)
    autor  = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=255)
    url_portada = models.CharField(max_length=40)

class Distopia(models.Model):
    titulo = models.CharField(max_length=40)
    autor  = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=255)
    url_portada = models.CharField(max_length=40)

class Fantasia(models.Model):
    titulo = models.CharField(max_length=40)
    autor  = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=255)
    url_portada = models.CharField(max_length=40)

