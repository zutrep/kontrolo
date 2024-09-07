from rest_framework import serializers
from restaurant.models import *

class MesaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mesa
        fields = ['__all__']

class MesaAtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesaAtencion
        fields = ['__all__']

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = ['__all__']

class PlatoSedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoSede
        fields = ['__all__']

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ['__all__']

