from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Materia (models.Model):
    nombreMateria = models.CharField(max_length=30, unique = True)
    clave = models.CharField(max_length=6, unique = True)
    grado = models.IntegerField(default=1)

    def __str__(self):
        return self.nombreMateria

class MateriaSecundaria (models.Model):
    nombreMateria = models.CharField(max_length=30, unique = True)
    clave = models.CharField(max_length=6, unique = True)
    grado = models.IntegerField(default=1)

    def __str__(self):
        return self.nombreMateria

class Alumno(models.Model):
    no_control = models.AutoField(primary_key=True)
    pin = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length = 20, null = True, blank=True)
    apellido_materno = models.CharField(max_length = 20, null=True , blank = True)
    nivel_educativo = models.CharField(max_length = 20, null=True , blank = True)
    grado = models.IntegerField(default=1)
    telefono = models.CharField(max_length = 10)
    domicilio = models.CharField(max_length=50)
    
    class Meta:
        verbose_name="alumnos"
        verbose_name_plural="alumnos"

    def __str__(self):
        return "%s %s %s %s" %(self.no_control,self.nombre, self.apellido_paterno, self.apellido_materno) 

class AlumnoSecundaria(models.Model):
    no_control = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length = 20, null = True, blank=True)
    apellido_materno = models.CharField(max_length = 20, null=True , blank = True)
    nivel_educativo = models.CharField(max_length = 20, null=True , blank = True)
    grado = models.IntegerField(default=1)
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
    
    class Meta:
        verbose_name="Docente"
        verbose_name_plural="Docentes"

    def __str__(self):
        return self.nombreDocente

class DocenteSecundaria (models.Model):
    
    nombreDocente = models.CharField(max_length=100)
    apellido_paterno_docente = models.CharField(max_length = 20, null = True, blank=True)
    apellido_materno_docente = models.CharField(max_length = 20, null=True , blank = True)
    correo = models.CharField(max_length=45)
    telefono = models.IntegerField()
    domicilio = models.CharField(max_length=50)
    registro = models.CharField(max_length=15)
    
    class Meta:
        verbose_name="DocenteSecundaria"
        verbose_name_plural="DocentesSecundaria"

    def __str__(self):
        return self.nombreDocente

class Calificaciones (models.Model):
    
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE )
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE)
    grado = models.IntegerField(default=1)
    Unidad1 = models.IntegerField(default=0)
    Unidad2 = models.IntegerField(default=0)
    Unidad3 = models.IntegerField(default=0)
    Unidad4 = models.IntegerField(default=0)
    Unidad5 = models.IntegerField(default=0)

    class Meta:
        verbose_name="Calificaciones"
        verbose_name_plural="Calificaciones"

    def unicode(self):
        return self.alumno



class CalificacionesSecundaria (models.Model):
    
    alumno = models.ForeignKey(AlumnoSecundaria, on_delete = models.CASCADE )
    materia = models.ForeignKey(MateriaSecundaria, on_delete = models.CASCADE)
    grado = models.IntegerField(default=1)
    Unidad1 = models.IntegerField(default=0)
    Unidad2 = models.IntegerField(default=0)
    Unidad3 = models.IntegerField(default=0)
    Unidad4 = models.IntegerField(default=0)
    Unidad5 = models.IntegerField(default=0)

    class Meta:
        verbose_name="Calificaciones"
        verbose_name_plural="Calificaciones"

    def unicode(self):
        return self.alumno

class Horario (models.Model):
    
    docente = models.ForeignKey(DocenteSecundaria, on_delete = models.CASCADE )
    materia = models.ForeignKey(MateriaSecundaria, on_delete = models.CASCADE)
    grado = models.IntegerField(default=1)
    Dia1 = models.TimeField()
    Dia2 = models.TimeField()
    Dia3 = models.TimeField()
    Dia4 = models.TimeField()
    Dia5 = models.TimeField()

    class Meta:
        verbose_name="Horario"
        verbose_name_plural="Horarios"

    def unicode(self):
        return self.docente