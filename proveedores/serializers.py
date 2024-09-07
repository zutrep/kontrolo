from rest_framework import serializers
from proveedores.models import *

class TipoProveedorSerializer(serializers.ModelSerializer):
    proveedores = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = TipoProveedor
        fields = ['__all__', 'proveedores']

class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = ['__all__']
