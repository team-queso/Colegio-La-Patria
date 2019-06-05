from django.db import models


class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol_asignable = models.CharField(max_length = 10 , unique = True)

    def __str__(self):
            return self.rol_asignable


class Usuario(models.Model):
    usuario = models.CharField( null = True, blank = True, max_length=20,unique = True)
    password = models.CharField(max_length=15)
    id_rol = models.ForeignKey(Roles, null = True, blank = True, on_delete= models.CASCADE)
    def __str__(self):
            return self.id_rol

