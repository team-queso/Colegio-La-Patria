from django.db import models

# Create your models here.
class administrador(models.Model):
    usuario = models.CharField(max_length=40)
    password = models.CharField(max_length=15)
    def __str__(self):
            return self.usuario

class alumno(models.Model):
    no_control = models.IntegerField()
    pin = models.IntegerField()
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    domicilio = models.CharField(max_length=150)
    grado = models.IntegerField(blank="false")
    grupo = models.CharField(blank="false", max_length=1)
    ciclo = models.CharField(max_length=9)

    def __str__(self):
        return self.no_control    
class grupos(models.Model):
    grupo = models.CharField(max_length=2)
    hora = models.CharField(max_length=11)
    aula = models.CharField(max_length=3)

    def __str__(self):
        return self.grupo
class docente (models.Model):
    nombreDocente = models.CharField(max_length=100)
    correo = models.CharField(max_length=45)
    telefono = models.IntegerField()
    domicilio = models.CharField(max_length=50)
    registro = models.CharField(max_length=15)
    pin = models.IntegerField()
class materia (models.Model):
    materia = models.CharField(max_length=45)
    clavemateria = models.IntegerField()

    def __str__(self):
        return self.materia

