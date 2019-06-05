# Generated by Django 2.1.7 on 2019-05-13 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0015_auto_20190513_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='id_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.Usuario'),
        ),
        migrations.AlterField(
            model_name='reticula',
            name='grupoAsignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.Grupos'),
        ),
        migrations.AlterField(
            model_name='reticula',
            name='materiaAsignada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.Materia'),
        ),
    ]
