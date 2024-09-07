from rest_framework import serializers
from ventas.models import *

class BoletaSerializer(serializers.ModelSerializer):
    detalles_boleta = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Boleta
        fields = ['__all__', 'detalle_boleta']

class BoletaDetalleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BoletaDetalle
        fields = ['__all__']

class FacturaSerializer(serializers.ModelSerializer):
    detalles_factura = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Factura
        fields = ['__all__','detalles_factura']

class FacturaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaDetalle
        fields = ['__all__']

class RecetaBoletaSerializer(serializers.ModelSerializer):
    detalles_receta_boleta = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = RecetaBoleta
        fields = ['__all__', 'detalles_receta_boleta']

class RecetaBoletaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaBoletaDetalle
        fields = ['__all__']

class RecetaFacturaSerializer(serializers.ModelSerializer):
    detalles_receta_factura = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = RecetaFactura
        fields = ['__all__', 'detalles_receta_factura']

class RecetaFacturaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaFacturaDetalle
        fields = ['__all__']

