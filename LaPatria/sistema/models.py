from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Materia (models.Model):
    nombreMateria = models.CharField(max_length=30, unique = True)
    clave = models.CharField(max_length=6, unique = True)

    def __str__(self):
        return self.nombreMateria

class Ciclo_escolar(models.Model):
    clave = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    finalizado = models.BooleanField(default=False)
    fecha_registro = models.DateField(auto_now=True)

    def __str__(self):
        return "%s %s %s" %(self.clave,self.fecha_inicio,self.fecha_termino)

    class Meta:
        verbose_name="ciclo_escolar"
        verbose_name_plural="ciclo_escolar"
class Grados(models.Model):
    clave = models.CharField(max_length=50)
    materias = models.ManyToManyField(Materia)
    fecha_registro = models.DateField(auto_now=True)

    def __str__(self):
        return self.clave

    class Meta:
        verbose_name="grados"
        verbose_name_plural="grados"
class Alumno(models.Model):
    no_control = models.AutoField(primary_key=True)
    pin = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length = 20, null = True, blank=True)
    apellido_materno = models.CharField(max_length = 20, null=True , blank = True)
    telefono = models.CharField(max_length = 10)
    domicilio = models.CharField(max_length=50)
    
    class Meta:
        verbose_name="alumnos"
        verbose_name_plural="alumnos"

    def __str__(self):
        return "%s %s %s %s" %(self.no_control,self.nombre, self.apellido_paterno, self.apellido_materno) 



class Docente (models.Model):
    
    nombreDocente = models.CharField(max_length=100)
    apellido_paterno_docente = models.CharField(max_length = 20, null = True, blank=True)
    apellido_materno_docente = models.CharField(max_length = 20, null=True , blank = True)
    correo = models.CharField(max_length=45)
    telefono = models.IntegerField()
    domicilio = models.CharField(max_length=50)
    registro = models.CharField(max_length=15)
    



    def __str__(self):
        return self.nombreDocente
class Unidad (models.Model):
    nombre = models.CharField(max_length=100)
    puntuacion = models.IntegerField()
    grado = models.ForeignKey(Grados, null = True, blank = True, on_delete= models.CASCADE)
    materia = models.ForeignKey(Materia, null = True, blank = True, on_delete= models.CASCADE)
    fecha_registro = models.DateField(auto_now=True)

    def __str__(self):
        return "%s %s"%(self.nombre,self.materia)

class UnidadCalificada (models.Model):
    unidad = models.ForeignKey(Unidad, null = True, blank = True, on_delete= models.CASCADE)
    puntuacion_asignada = models.IntegerField()
    alumno = models.ForeignKey(Alumno,null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.unidad,self.alumno,self.puntuacion_asignada)
