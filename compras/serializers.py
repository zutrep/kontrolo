from rest_framework import serializers
from compras.models import *

class BoletaCompraSerializer(serializers.ModelSerializer):
    detalles_boleta = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = BoletaCompra
        fields = ['__all__', 'detalle_boleta']

class BoletaCompraDetalleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BoletaCompraDetalle
        fields = ['__all__']

class FacturaCompraSerializer(serializers.ModelSerializer):
    detalles_factura = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = FacturaCompra
        fields = ['__all__','detalles_factura']

class FacturaCompraDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaCompraDetalle
        fields = ['__all__']
