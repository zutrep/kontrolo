from django.db import models
from logistica.models import Producto

class Impuesto(models.Model):
    nombre = models.CharField(max_length=250)
    tipo = models.SmallIntegerField() 
    #negativo para impuestos que restan positivo para los que suman
    porcentaje = models.SmallIntegerField()


class ImpuestoProducto(models.Model):
    producto_id=models.ForeignKey(Producto, on_delete=models.CASCADE)
    impuesto_id = models.ForeignKey(Impuesto, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField()



