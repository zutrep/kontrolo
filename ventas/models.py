from django.db import models
from logistica.models import Producto
from portafolio.models import Cliente
from restaurant.models import Receta
from django.utils import timezone

class Boleta(models.Model):
    codigo = models.BigIntegerField()
    subtotal = models.IntegerField()
    impuestos = models.IntegerField()
    total = models.IntegerField()
    
    def __str__(self):
        return (self.codigo)    

class BoletaDetalle(models.Model):
    boleta_id = models.ForeignKey(Boleta, related_name='detalles_boleta', on_delete=models.PROTECT)
    producto_id = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now())
    estado = models.PositiveSmallIntegerField()

class Factura(models.Model):
    codigo = models.BigIntegerField()
    cliente_id = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    subtotal = models.IntegerField()
    impuestos = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return (self.codigo)  
    
class FacturaDetalle(models.Model):
    factura_id = models.ForeignKey(Factura,related_name='detalles_factura', on_delete=models.PROTECT)
    producto_id = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now())
    estado = models.PositiveSmallIntegerField()


class RecetaBoleta(models.Model):
    codigo = models.BigIntegerField()
    subtotal = models.IntegerField()
    impuestos = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return (self.codigo) 
    
class RecetaBoletaDetalle(models.Model):
    receta_boleta_id = models.ForeignKey(RecetaBoleta,related_name='detalles_receta_boleta', on_delete=models.PROTECT)
    receta_id = models.ForeignKey(Receta, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now())
    estado = models.PositiveSmallIntegerField()



class RecetaFactura(models.Model):
    codigo = models.BigIntegerField()
    cliente_id = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    subtotal = models.IntegerField()
    impuestos = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return (self.codigo) 

class RecetaFacturaDetalle(models.Model):
    receta_factura_id = models.ForeignKey(Factura, related_name='detalles_receta_factura', on_delete=models.PROTECT)
    receta_id = models.ForeignKey(Receta, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now())
    estado = models.PositiveSmallIntegerField()







