from rest_framework import serializers
from logistica.models import *
from restaurant.models import *

class SedeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sede
        fields = [
            'nombre',
            'direccion',
            'estado',
            'fecha_creacion',
            'empresa'
        ]

class AlmacenSerializer(serializers.ModelSerializer):
    productos = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Almacen
        fields = '__all__'

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    almacenes = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Producto
        fields = ['__all__', 'almacenes']

class InventarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventario
        fields = '__all__'

class IngresoInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngresoInventario
        fields = '__all__'

class SalidaInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalidaInventario
        fields = '__all__'
