# Generated by Django 5.1.1 on 2024-09-07 16:31

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_recetaboletadetalle_receta_boleta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recetaboletadetalle',
            old_name='receta_boleta',
            new_name='receta_boleta_id',
        ),
        migrations.AddField(
            model_name='boleta',
            name='codigo',
            field=models.BigIntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boletadetalle',
            name='boleta_id',
            field=models.ForeignKey( on_delete=django.db.models.deletion.PROTECT, to='ventas.boleta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factura',
            name='codigo',
            field=models.BigIntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facturadetalle',
            name='factura_id',
            field=models.ForeignKey( on_delete=django.db.models.deletion.PROTECT, to='ventas.factura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recetaboleta',
            name='codigo',
            field=models.BigIntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recetafactura',
            name='codigo',
            field=models.BigIntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recetafacturadetalle',
            name='receta_factura_id',
            field=models.ForeignKey( on_delete=django.db.models.deletion.PROTECT, to='ventas.factura'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boletadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 16, 30, 35, 932121, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='facturadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 16, 30, 35, 933625, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='recetaboletadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 16, 30, 35, 933625, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='recetafacturadetalle',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 16, 30, 35, 935135, tzinfo=datetime.timezone.utc)),
        ),
    ]
