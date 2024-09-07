from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from login.serializers import *



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all().order_by('razon_social')
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('email')
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all().order_by('nombre')
    serializer_class = GrupoSerializer
    permission_classes = [permissions.IsAuthenticated]


class HerramientaViewSet(viewsets.ModelViewSet):
    queryset = Herramienta.objects.all()
    serializer_class = HerramientaSerializer
    permission_classes = [permissions.IsAuthenticated]

class HerramientaGrupoViewSet(viewsets.ModelViewSet):
    queryset = HerramientaGrupo.objects.all()
    serializer_class = HerramientaGrupoSerializer
    permission_classes = [permissions.IsAuthenticated]

class HerramientaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = HerramientaUsuario.objects.all()
    serializer_class = HerramientaUsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermisoGrupoViewSet(viewsets.ModelViewSet):
    queryset = PermisoGrupo.objects.all()
    serializer_class = PermisoGrupoSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermisoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PermisoUsuario.objects.all()
    serializer_class = PermisoUsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer
    permission_classes = [permissions.IsAdminUser]