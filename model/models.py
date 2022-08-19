from django.db import models


class familiares(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha = models.DateField()