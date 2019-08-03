# Generated by Django 2.1.7 on 2019-07-20 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0046_auto_20190720_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificaciones',
            name='grado',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='calificaciones',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Alumno'),
        ),
    ]