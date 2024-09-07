from rest_framework import serializers
from contabilidad.models import *

class ImpuestoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Impuesto
        fields = ['__all__']

class ImpuestoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpuestoProducto
        fields = ['__all__']



