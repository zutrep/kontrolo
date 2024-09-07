from django.db import models
from django.utils import timezone

class TipoCliente(models.Model):
    nombre = models.CharField(max_length=200)
    #natural o juridico

    def __str__(self):
        return (self.nombre)

class Cliente(models.Model):
    razon_social = models.TextField(null=False)
    registro = models.CharField(max_length=250, unique=True)
    direccion = models.CharField(max_length=250, null=True)
    tipo_cliente = models.ForeignKey(TipoCliente,related_name='clientes', on_delete=models.PROTECT)
    estado = models.SmallIntegerField(default=1)
    fecha_creacion = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return (self.registro + ' - ' +self.razon_social)


    