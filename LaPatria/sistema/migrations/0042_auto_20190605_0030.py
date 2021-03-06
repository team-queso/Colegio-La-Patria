# Generated by Django 2.1.7 on 2019-06-05 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0041_auto_20190605_0015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumno',
            options={'verbose_name': 'alumnos', 'verbose_name_plural': 'alumnos'},
        ),
        migrations.RemoveField(
            model_name='unidadcalificada',
            name='materia',
        ),
        migrations.AlterField(
            model_name='unidadcalificada',
            name='alumno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.Alumno'),
        ),
        migrations.AlterField(
            model_name='unidadcalificada',
            name='unidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.Unidad'),
        ),
    ]
