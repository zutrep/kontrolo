from django.db import models
from login.models import Usuario
from logistica.models import Sede, Producto
from django.utils import timezone



class Mesa(models.Model):
    sede_id = models.ForeignKey(Sede, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    aforo = models.SmallIntegerField()
    ocupada = models.SmallIntegerField(default=0)
    estado = models.SmallIntegerField(default=1)
    fecha_creacion = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return (self.nombre)
    
class MesaAtencion(models.Model):
    mesa_id = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_atencion = models.DateField(default=timezone.now())


class Plato(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(default=timezone.now())
    estado = models.SmallIntegerField(default=0)
    precio = models.IntegerField(null=True)
    
    def __str__(self):
        return (self.nombre)
    
class PlatoSede(models.Model):
    plato_id = models.ForeignKey(Plato, on_delete=models.CASCADE)
    sede_id = models.ForeignKey(Sede, on_delete=models.CASCADE)

class Receta(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    plato_id = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()







    


    
















