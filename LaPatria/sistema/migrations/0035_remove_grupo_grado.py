# Generated by Django 2.1.7 on 2019-05-23 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0034_auto_20190523_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='grado',
        ),
    ]
