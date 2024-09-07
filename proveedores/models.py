from django.db import models
from django.utils import timezone

class TipoProveedor(models.Model):
    nombre = models.CharField(max_length=200)
    #natural o juridico

    def __str__(self):
        return (self.nombre)
    
class Proveedor(models.Model):
    razon_social = models.TextField(null=False)
    registro = models.CharField(max_length=250, unique=True)
    direccion = models.CharField(max_length=250, null=True)
    estado = models.SmallIntegerField(default=1)
    fecha_creacion = models.DateTimeField(default=timezone.now())
    tipo_proveedor = models.ForeignKey(TipoProveedor,related_name='proveedores', on_delete=models.PROTECT)


    def __str__(self):
        return (self.registro + ' - ' +self.razon_social)
