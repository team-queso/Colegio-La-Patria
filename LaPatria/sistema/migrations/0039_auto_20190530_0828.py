# Generated by Django 2.1.7 on 2019-05-30 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0038_auto_20190530_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificación',
            name='alumno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.Alumno'),
        ),
    ]