# Generated by Django 2.1.7 on 2019-07-20 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0045_auto_20190718_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificaciones',
            name='Calificacion',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='Unidad',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='grado',
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='Unidad1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='Unidad2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='Unidad3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='Unidad4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='Unidad5',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calificaciones',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Alumno'),
        ),
    ]
