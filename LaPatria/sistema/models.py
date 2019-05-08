from django.db import models

# Create your models here.
class administrador(models.Model):
    usuario = models.CharField(max_length=40)
    password = models.CharField(max_length=15)
    def __str__(self):
            return self.usuario
class Materia (models.Model):
    materia = models.CharField(max_length=45)
    claveMateria = models.CharField(max_length=6, null= True)

    def __str__(self):
        return '{}' .format(self.materia)
class Grupos(models.Model):
    grupo = models.CharField(max_length=2)
    ciclo = models.CharField(max_length=9, null=True)
    

    def __str__(self):
        return '{}' .format(self.grupo)
    

class Reticula(models.Model):
    periodo = models.CharField(null = True, blank = True, max_length=12)
    materiaAsignada = models.ForeignKey(Materia, null = True, blank = True, on_delete=models.CASCADE)
    grupoAsignado = models.ForeignKey(Grupos, null = True, blank = True, on_delete=models.CASCADE)
    

    def __str__(self):
        return '{} ' .format(self.grupoAsignado)


class Alumno(models.Model):
    no_control = models.AutoField(primary_key=True)
    pin = models.IntegerField()
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    domicilio = models.CharField(max_length=150)
    reticula = models.ForeignKey(Reticula, null = True, blank = True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre   



class Docente (models.Model):
    nombreDocente = models.CharField(max_length=100)
    correo = models.CharField(max_length=45)
    telefono = models.IntegerField()
    domicilio = models.CharField(max_length=50)
    registro = models.CharField(max_length=15)
    pin = models.IntegerField()


    def __str__(self):
        return self.nombreDocente




