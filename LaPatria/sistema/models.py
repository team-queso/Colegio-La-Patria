from django.db import models

# Create your models here.
class admin(models.Model):
    usuario = models.CharField(max_length=40)
    password = models.CharField(max_length=15)

