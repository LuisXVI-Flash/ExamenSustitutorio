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

