# Generated by Django 5.1.1 on 2024-09-08 21:41

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_usuario_last_login_alter_empleado_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='usuario',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name='empresas', to='login.usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 41, 13, 314827, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 41, 13, 314827, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 41, 13, 313303, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='herramientaempleado',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 41, 13, 314827, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='herramientagrupo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 41, 13, 314827, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisoempleado',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 41, 13, 319421, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisogrupo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 41, 13, 319421, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sesionempleado',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 41, 13, 319421, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sesionusuario',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 41, 13, 319421, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 21, 41, 13, 314322, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='UsuarioEmpresa',
        ),
    ]
