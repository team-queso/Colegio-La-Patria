# Generated by Django 2.1.7 on 2019-04-25 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0010_auto_20190425_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reticula',
            name='cicloEscolar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ciclo_Grupos', to='sistema.Grupos'),
        ),
        migrations.AlterField(
            model_name='reticula',
            name='grupoAsignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grupo_Grupos', to='sistema.Grupos'),
        ),
        migrations.AlterField(
            model_name='reticula',
            name='materiaAsignada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.Materia'),
        ),
    ]
