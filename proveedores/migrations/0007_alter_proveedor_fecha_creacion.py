# Generated by Django 5.1.1 on 2024-09-07 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0006_alter_proveedor_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 22, 54, 32, 141525, tzinfo=datetime.timezone.utc)),
        ),
    ]
