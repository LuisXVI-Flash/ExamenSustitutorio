from django.db import models

# Create your models here.
class Libro(models.Model):
    idlibro = models.IntegerField()
    nombre = models.CharField(max_length=20)
    codigo = models.IntegerField()
    fecha = models.CharField(max_length=10)
    stock = models.IntegerField()
    idautores = models.IntegerField()
    ideditorial = models.IntegerField()
    idpais = models.IntegerField()

class Autor(models.Model):
    idautor = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    dni = models.IntegerField()
    estado = models.CharField(max_length=1)

class Editoriales(models.Model):
    ideditorial = models.IntegerField()
    nombre = models.CharField(max_length=40)
    estado = models.CharField(max_length=1)

class Pais(models.Model):
    idpais = models.IntegerField()
    nombre = models.CharField(max_length=20)
    estado = models.CharField(max_length=1)


