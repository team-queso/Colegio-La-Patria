# Generated by Django 2.1.7 on 2019-05-23 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0036_grupo_grado'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='id_grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.Grupo'),
        ),
        migrations.AddField(
            model_name='docente',
            name='id_grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.Grupo'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='nombreMateria',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
