# Generated by Django 5.1.1 on 2024-09-08 03:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_alter_empleado_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 3, 26, 12, 62465, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 3, 26, 12, 62465, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 3, 26, 12, 61243, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='herramientaempleado',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 3, 26, 12, 62465, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='herramientagrupo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 3, 26, 12, 62465, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisoempleado',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 3, 26, 12, 62465, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisogrupo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 3, 26, 12, 62465, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sesionempleado',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 3, 26, 12, 64742, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sesionusuario',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 3, 26, 12, 62465, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 3, 26, 12, 61243, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
    ]
