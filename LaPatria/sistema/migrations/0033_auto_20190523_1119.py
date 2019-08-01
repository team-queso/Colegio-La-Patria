# Generated by Django 2.1.7 on 2019-05-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0032_auto_20190523_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia_grupo',
            name='id_Alumno',
        ),
        migrations.RemoveField(
            model_name='materia_grupo',
            name='id_Docente',
        ),
        migrations.RemoveField(
            model_name='materia_grupo',
            name='id_Grupo',
        ),
        migrations.RemoveField(
            model_name='materia_grupo',
            name='id_Materia',
        ),
        migrations.AddField(
            model_name='grupo',
            name='materia',
            field=models.ManyToManyField(to='sistema.Materia'),
        ),
        migrations.DeleteModel(
            name='Materia_grupo',
        ),
    ]