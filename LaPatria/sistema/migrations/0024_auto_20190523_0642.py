# Generated by Django 2.1.7 on 2019-05-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0023_auto_20190523_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='grado',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='grupo',
            field=models.CharField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), (6, 'F')], default=1, max_length=1),
        ),
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
