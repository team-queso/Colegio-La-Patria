# Generated by Django 2.1.7 on 2019-08-05 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0056_auto_20190805_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Alumno'),
        ),
    ]
