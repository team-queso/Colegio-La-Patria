from django.db import models

# Create your models here.
class administrador(models.Model):
    usuario = models.CharField(max_length=40)
    password = models.CharField(max_length=15)

