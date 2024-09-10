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
    empleados = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Empresa
        fields = ['url', 'razon_social', 
                  'registro','direccion','estado',
                  'fecha_creacion', 'usuarios', 'sedes', 'empleados']
        

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    empresas = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'email',
            'password',
            'estado',
            'fecha_creacion',
            'empresas'
        ]
        

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = [
            'nombre',
            'email',
            'password',
            'estado',
            'fecha_creacion',
            'grupo_id',
            'empresa_id'
        ]

class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    herramientas = serializers.StringRelatedField(many=True, read_only=True)
    empleados_grupo = serializers.StringRelatedField(many=True, read_only=True)
    permisos = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Grupo
        fields = [
            'nombre',
            'fecha_creacion',
            'url',
            'herramientas',
            'empleados_grupo',
            'permisos'
        ]


class HerramientaSerializer(serializers.HyperlinkedModelSerializer):
    grupos = serializers.StringRelatedField(many=True, read_only=True)
    herramientas_empleado =serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Herramienta
        fields = [
            'nombre',
            'estado',
            'posicion',
            'url',
            'grupos',
            'herramientas_empleado'
        ]

class HerramientaGrupoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HerramientaGrupo
        fields = [
            'herramienta',
            'grupo',
            'fecha_creacion'
        ]

class HerramientaEmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HerramientaEmpleado
        fields = [
            'herramienta_id',
            'empleado_id',
            'fecha_creacion'
        ]
    
class PermisoSerializer(serializers.HyperlinkedModelSerializer):
    grupos_permiso = serializers.StringRelatedField(many=True, read_only=True)
    permisos_grupo = serializers.StringRelatedField(many=True, read_only=True)
   
    class Meta:
        model = Permiso
        fields = [
            'nombre',
            'grupos_permiso',
            'permisos_grupo'
        ]

class PermisoGrupoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PermisoGrupo
        fields = [
        'permiso_id',
        'grupo_id',
        'fecha_creacion'
        ]

class PermisoEmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PermisoEmpleado
        fields = [
        'permiso_id',
        'empleado_id',
        'fecha_creacion'
        ]

class SesionUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SesionUsuario
        fields = [
            'usuario_id',
            'token',
            'fecha_creacion'
        ]

class SesionEmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SesionEmpleado
        fields = [
            'empleado_id',
            'token',
            'fecha_creacion'
        ]