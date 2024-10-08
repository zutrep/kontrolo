# Generated by Django 5.1.1 on 2024-09-07 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_alter_empresa_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 865075, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 903960, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='herramientagrupo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 903960, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='herramientausuario',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 903960, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisogrupo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 903960, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisousuario',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 903960, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 903960, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 903960, tzinfo=datetime.timezone.utc)),
        ),
    ]
