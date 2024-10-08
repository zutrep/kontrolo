# Generated by Django 5.1.1 on 2024-09-07 15:38

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='herramientagrupo',
            name='grupo_id',
        ),
        migrations.RemoveField(
            model_name='grupousuario',
            name='grupo_id',
        ),
        migrations.RemoveField(
            model_name='permisogrupo',
            name='grupo_id',
        ),
        migrations.RemoveField(
            model_name='grupousuario',
            name='usuario_id',
        ),
        migrations.RemoveField(
            model_name='herramientausuario',
            name='herramienta_id',
        ),
        migrations.RemoveField(
            model_name='herramientagrupo',
            name='herramienta_id',
        ),
        migrations.RemoveField(
            model_name='herramientausuario',
            name='usuario_id',
        ),
        migrations.RemoveField(
            model_name='permisousuario',
            name='permiso_id',
        ),
        migrations.RemoveField(
            model_name='permisogrupo',
            name='permiso_id',
        ),
        migrations.RemoveField(
            model_name='permisousuario',
            name='usuario_id',
        ),
        migrations.RemoveField(
            model_name='sesion',
            name='usuario_id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='proveedor_id',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='fecha_Creacion',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='tipo_proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='proveedores', to='proveedores.tipoproveedor'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Grupo',
        ),
        migrations.DeleteModel(
            name='GrupoUsuario',
        ),
        migrations.DeleteModel(
            name='Herramienta',
        ),
        migrations.DeleteModel(
            name='HerramientaGrupo',
        ),
        migrations.DeleteModel(
            name='HerramientaUsuario',
        ),
        migrations.DeleteModel(
            name='Permiso',
        ),
        migrations.DeleteModel(
            name='PermisoGrupo',
        ),
        migrations.DeleteModel(
            name='PermisoUsuario',
        ),
        migrations.DeleteModel(
            name='Sesion',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 15, 38, 45, 690055, tzinfo=datetime.timezone.utc)),
        ),
    ]
