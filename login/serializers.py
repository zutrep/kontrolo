from django.contrib.auth.models import Group, User
from rest_framework import serializers
from login.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    usuarios = serializers.StringRelatedField(many=True, read_only=True)
    sedes = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Empresa
        fields = ['url', 'razon_social', 
                  'registro','direccion','estado',
                  'fecha_creacion', 'usuarios', 'sedes']
        

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    herramientas = serializers.StringRelatedField(many=True, read_only=True)
    permisos = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Usuario
        fields = [
            '__all__',
            'herramientas',
            'permisos'
        ]
        

class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    herramientas = serializers.StringRelatedField(many=True, read_only=True)
    usuarios_grupo = serializers.StringRelatedField(many=True, read_only=True)
    permisos = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Grupo
        fields = [
            'nombre',
            'fecha_creacion',
            'url',
            'herramientas',
            'usuarios_grupo',
            'permisos'
        ]


class HerramientaSerializer(serializers.HyperlinkedModelSerializer):
    grupos = serializers.StringRelatedField(many=True, read_only=True)
    herramientas_usuario =serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Herramienta
        fields = [
            'nombre',
            'estado',
            'posicion',
            'url',
            'grupos',
            'herramientas_usuario'
        ]

class HerramientaGrupoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HerramientaGrupo
        fields = [
            '__all__'
        ]

class HerramientaUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HerramientaUsuario
        fields = [
           '__all__'
        ]
    
class PermisoSerializer(serializers.HyperlinkedModelSerializer):
    grupos_permiso = serializers.StringRelatedField(many=True, read_only=True)
    permisos_grupo = serializers.StringRelatedField(many=True, read_only=True)
   
    class Meta:
        model = Permiso
        fields = [
            '__all__',
            'grupos_permiso',
            'permisos_grupo'
        ]

class PermisoGrupoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PermisoGrupo
        fields = [
           '__all__'
        ]

class PermisoUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PermisoUsuario
        fields = [
        '__all__'
        ]

class SesionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sesion
        fields = [
            '__all__'
        ]