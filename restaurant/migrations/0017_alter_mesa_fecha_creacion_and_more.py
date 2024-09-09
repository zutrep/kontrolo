# Generated by Django 5.1.1 on 2024-09-08 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_alter_mesa_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 46, 6, 296211, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='mesaatencion',
            name='fecha_atencion',
            field=models.DateField(default=datetime.datetime(2024, 9, 8, 21, 46, 6, 297425, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='plato',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 46, 6, 297425, tzinfo=datetime.timezone.utc)),
        ),
    ]
