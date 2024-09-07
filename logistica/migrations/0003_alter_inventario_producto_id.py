# Generated by Django 5.1.1 on 2024-09-07 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0002_alter_inventario_almacen_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='producto_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='almacenes', to='logistica.producto'),
        ),
    ]
