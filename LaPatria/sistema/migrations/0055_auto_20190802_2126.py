# Generated by Django 2.1.7 on 2019-08-03 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0054_auto_20190802_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Alumno'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Docente'),
        ),
    ]
