# Generated by Django 2.1.7 on 2019-04-24 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_auto_20190415_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_control', models.IntegerField()),
                ('pin', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('domicilio', models.CharField(max_length=150)),
                ('grado', models.IntegerField(blank='false')),
                ('grupo', models.CharField(blank='false', max_length=1)),
                ('ciclo', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDocente', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=45)),
                ('telefono', models.IntegerField()),
                ('domicilio', models.CharField(max_length=50)),
                ('registro', models.CharField(max_length=15)),
                ('pin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='grupos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(max_length=2)),
                ('hora', models.CharField(max_length=11)),
                ('aula', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=45)),
                ('clavemateria', models.IntegerField()),
            ],
        ),
    ]