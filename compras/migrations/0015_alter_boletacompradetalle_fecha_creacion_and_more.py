# Generated by Django 5.1.1 on 2024-09-09 02:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0014_alter_boletacompradetalle_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletacompradetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 2, 57, 2, 395824, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='facturacompradetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 2, 57, 2, 395824, tzinfo=datetime.timezone.utc)),
        ),
    ]
