from django.db import models
from logistica.models import Producto
from proveedores.models import Proveedor
from django.utils import timezone


class BoletaCompra(models.Model):
    codigo = models.BigIntegerField()
    subtotal = models.IntegerField()
    impuestos = models.IntegerField()
    total = models.IntegerField()
    
    def __str__(self):
        return (self.codigo)    

class BoletaCompraDetalle(models.Model):
    boleta_id = models.ForeignKey(BoletaCompra, related_name='detalles_boleta', on_delete=models.PROTECT)
    producto_id = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now())
    estado = models.PositiveSmallIntegerField()

class FacturaCompra(models.Model):
    codigo = models.BigIntegerField()
    proveedor_id = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    subtotal = models.IntegerField()
    impuestos = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return (self.codigo)  
    
class FacturaCompraDetalle(models.Model):
    factura_id = models.ForeignKey(FacturaCompra,related_name='detalles_factura', on_delete=models.PROTECT)
    producto_id = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now())
    estado = models.PositiveSmallIntegerField()








