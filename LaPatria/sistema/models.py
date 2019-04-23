from django.db import models

# Create your models here.
class administrador(models.Model):
    usuario = models.CharField(max_length=40)
    password = models.CharField(max_length=15)

class alumno(models.Model):
    idAlumno = models.IntegerField(max_length=45)
    no_control = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    telefono = models.IntegerField(max_length=10)
    domicilio = models.CharField(max_length=150)
    grado = models.IntegerField(max_length=1)
    ciclo = models.CharField(max_length=9)