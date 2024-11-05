from django.db import models

class Formulario(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_seminario = models.DateField()
    institucion = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)
