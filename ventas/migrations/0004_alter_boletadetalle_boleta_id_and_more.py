# Generated by Django 5.1.1 on 2024-09-07 17:04

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_rename_receta_boleta_recetaboletadetalle_receta_boleta_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletadetalle',
            name='boleta_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles_boleta', to='ventas.boleta'),
        ),
        migrations.AlterField(
            model_name='boletadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 913925, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='facturadetalle',
            name='factura_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles_factura', to='ventas.factura'),
        ),
        migrations.AlterField(
            model_name='facturadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 919566, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='recetaboletadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 919566, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='recetaboletadetalle',
            name='receta_boleta_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles_receta_boleta', to='ventas.recetaboleta'),
        ),
        migrations.AlterField(
            model_name='recetafacturadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 17, 4, 29, 919566, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='recetafacturadetalle',
            name='receta_factura_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles_receta_factura', to='ventas.factura'),
        ),
    ]
