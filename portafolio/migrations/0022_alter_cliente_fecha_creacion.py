# Generated by Django 5.1.1 on 2024-09-09 02:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0021_alter_cliente_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 2, 30, 54, 975902, tzinfo=datetime.timezone.utc)),
        ),
    ]
