# Generated by Django 2.1.7 on 2019-05-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0030_auto_20190523_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia_grupo',
            name='id_Alumno',
            field=models.ManyToManyField(to='sistema.Alumno'),
        ),
        migrations.AlterField(
            model_name='materia_grupo',
            name='id_Docente',
            field=models.ManyToManyField(to='sistema.Docente'),
        ),
    ]