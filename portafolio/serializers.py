from rest_framework import serializers
from portafolio.models import *

class TipoClienteSerializer(serializers.ModelSerializer):
    clientes = serializers.StringRelatedField(many=True, read_only=True)
   
    class Meta:
        model = TipoCliente
        fields = ['__all__','clientes']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['__all__']
