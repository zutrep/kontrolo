# Generated by Django 5.1.1 on 2024-09-09 02:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0017_alter_boletadetalle_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 2, 30, 54, 978415, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='facturadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 2, 30, 54, 980885, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='recetaboletadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 2, 30, 54, 980885, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='recetafacturadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 2, 30, 54, 980885, tzinfo=datetime.timezone.utc)),
        ),
    ]
