from django.db import models
from django.utils import timezone

class Empresa(models.Model):
    razon_social = models.TextField(null=False)
    registro = models.CharField(max_length=250, unique=True)
    direccion = models.CharField(max_length=250, null=True)
    estado = models.SmallIntegerField(default=1)
    fecha_creacion = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return (self.registro + ' - ' +self.razon_social)
    
class Grupo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return (self.nombre)

 
class Usuario(models.Model):
    nombre = models.CharField(max_length=250)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=250)
    estado = models.SmallIntegerField(default=1)
    fecha_creacion = models.DateTimeField(default=timezone.now())
    empresa_id = models.ForeignKey(Empresa,related_name='usuarios', on_delete=models.CASCADE)
    grupo_id = models.ForeignKey(Grupo,related_name='usuarios_grupo', on_delete=models.CASCADE)

    def __str__(self):
        return (self.nombre)
    


class Herramienta(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.SmallIntegerField(default=1)
    posicion = models.IntegerField()

    def __str__(self):
        return (self.nombre)

class HerramientaGrupo(models.Model):
    herramienta_id = models.ForeignKey(Herramienta,related_name='grupos', on_delete=models.CASCADE)
    grupo_id = models.ForeignKey(Grupo,related_name='herramientas', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now())
    
class HerramientaUsuario(models.Model):
    herramienta_id = models.ForeignKey(Herramienta,related_name='usuarios_herramienta', on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario,related_name='herramientas_usuario', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now())

class Permiso(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return (self.nombre)

class PermisoGrupo(models.Model):
    permiso_id = models.ForeignKey(Permiso,related_name='grupos_permiso', on_delete=models.CASCADE)
    grupo_id = models.ForeignKey(Grupo,related_name='permisos_grupo', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now())

class PermisoUsuario(models.Model):
    permiso_id = models.ForeignKey(Permiso, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now())

class Sesion(models.Model):
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    token = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(default=timezone.now())
