# Generated by Django 5.1.1 on 2024-09-08 02:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0007_alter_proveedor_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 2, 46, 19, 886047, tzinfo=datetime.timezone.utc)),
        ),
    ]
