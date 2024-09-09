# Generated by Django 5.1.1 on 2024-09-09 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0027_alter_empleado_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='usuario',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name='grupos', to='login.usuario'),
            preserve_default=False,
        ),
    ]
