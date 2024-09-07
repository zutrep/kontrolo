from django.db import models
from login.models import Empresa

class Sede(models.Model):
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250, null=True)
    estado = models.SmallIntegerField(default=1)
    fecha_creacion = models.DateTimeField()
    empresa_id = models.ForeignKey(Empresa, related_name='sedes', on_delete=models.CASCADE)

    def __str__(self):
        return (self.nombre)

class Almacen(models.Model):
    nombre = models.CharField(max_length=250)
    sede_id = models.ForeignKey(Sede, on_delete=models.CASCADE)
    metros = models.SmallIntegerField(null=True)

    def __str__(self):
        return (self.nombre)

class Unidad(models.Model):
    nombre = models.CharField(max_length=50)
    unidades = models.IntegerField(null=True)

    def __str__(self):
        return (self.nombre)
    #si la unidad no contiene unidades este campo permanece null 
    #ejemplo una caja de cerveza contiene 12 cervezas

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField()
    unidad_id = models.ForeignKey(Unidad, on_delete=models.PROTECT)

    def __str__(self):
        return (self.nombre)

class Inventario(models.Model):
    producto_id = models.ForeignKey(Producto,related_name='almacenes', on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=0)
    almacen_id = models.ForeignKey(Almacen,related_name='productos', on_delete=models.PROTECT)
    
class IngresoInventario(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.PROTECT)
    almacen_id = models.ForeignKey(Almacen, on_delete=models.PROTECT)
    costo_unitario = models.PositiveIntegerField(default=0)
    cantidad = models.PositiveIntegerField()
    costo_total = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField()

class SalidaInventario(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.PROTECT)
    almacen_id = models.ForeignKey(Almacen, on_delete=models.PROTECT)
    costo_unitario = models.PositiveIntegerField(default=0)
    cantidad = models.PositiveIntegerField()
    costo_total = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField()