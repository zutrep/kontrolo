# Generated by Django 5.1.1 on 2024-09-06 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.SmallIntegerField(default=1)),
                ('posicion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.TextField()),
                ('registro', models.CharField(max_length=250, unique=True)),
                ('direccion', models.CharField(max_length=250, null=True)),
                ('estado', models.SmallIntegerField(default=1)),
                ('fecha_Creacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HerramientaGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField()),
                ('grupo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.grupo')),
                ('herramienta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.herramienta')),
            ],
        ),
        migrations.CreateModel(
            name='PermisoGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField()),
                ('grupo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.grupo')),
                ('permiso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.permiso')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=250)),
                ('estado', models.SmallIntegerField(default=1)),
                ('fecha_creacion', models.DateTimeField()),
                ('proveedor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=250)),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='PermisoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField()),
                ('permiso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.permiso')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='HerramientaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField()),
                ('herramienta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.herramienta')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='GrupoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.grupo')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.usuario')),
            ],
        ),
    ]
