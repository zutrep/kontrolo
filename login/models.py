from django.db import models
from django.utils import timezone




class Usuario(models.Model):
    nombre = models.CharField(max_length=250)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=250)
    estado = models.SmallIntegerField(default=1)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)


class Empresa(models.Model):
    razon_social = models.TextField(null=False)
    registro = models.CharField(max_length=250, unique=True)
    direccion = models.CharField(max_length=250, null=True)
    estado = models.SmallIntegerField(default=1)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario,related_name='empresas', on_delete=models.CASCADE)
    
class Grupo(models.Model):
    usuario = models.ForeignKey(Usuario,related_name='grupos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    estado = models.SmallIntegerField(default=1)

class Empleado(models.Model):
    nombre = models.CharField(max_length=250)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=250)
    estado = models.SmallIntegerField(default=1)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)
    empresa = models.ForeignKey(Empresa,related_name='empleados', on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,related_name='empleados_grupo', on_delete=models.CASCADE)

class Herramienta(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.SmallIntegerField(default=1)
    posicion = models.IntegerField()

class HerramientaGrupo(models.Model):
    herramienta = models.ForeignKey(Herramienta,related_name='grupos', on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,related_name='herramientas', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
class HerramientaEmpleado(models.Model):
    herramienta = models.ForeignKey(Herramienta,related_name='empleados_herramienta', on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado,related_name='herramientas_empleado', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)

class Permiso(models.Model):
    nombre = models.CharField(max_length=250)

class PermisoGrupo(models.Model):
    permiso = models.ForeignKey(Permiso,related_name='grupos_permiso', on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,related_name='permisos_grupo', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)

class PermisoEmpleado(models.Model):
    permiso = models.ForeignKey(Permiso, related_name='empleados_permiso', on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado,related_name='permisos_empleado', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)

class SesionUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    token = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(default=timezone.now)

class SesionEmpleado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    token = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(default=timezone.now)