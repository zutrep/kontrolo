from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from login import permisos
from login.models import Usuario, SesionUsuario
from rest_framework.response import Response
from django.utils import timezone
from login.serializers import *
from rest_framework.authtoken.models import Token
from jose import jws
import base64

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



class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('email')
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]




    def create(self,request):
        #respuesta = Response(request.data)
        #return respuesta
        nombre = None
        try:
            nombre = request.data['nombre']
        except:
            pass

        email = request.data['email']
        password = request.data['password']

        if not nombre:
            today = timezone.now()
            usuario = None
            try:
                usuario = Usuario.objects.get(email=email,password=password)
                usuario.last_login = today
                usuario.save() 
            except:
                pass

            if usuario:
                existe_sesion = None
                try:
                    existe_sesion = SesionUsuario.objects.get(usuario_id=usuario.id)
                except:
                    pass

                if existe_sesion:
                    existe_sesion.delete()
                
                key = str(usuario.last_login)
                claim = base64.b64encode(bytes(key.encode('utf-8')))
                token = jws.sign(claim, key, algorithm='HS256')
              
                #generar sesion de ususario
                sesion = SesionUsuario(token=token,usuario_id=usuario.id)
                sesion.save()
                token = None
                return Response({'respuesta':True,'mensaje':'login exitoso','token':sesion.token})
            else:
                return Response({'respuesta':False,'mensaje':'usuario o password incorrectos'})
        else:
            try:
                usuario = Usuario(nombre=nombre,email=email,password=password)
                usuario.save()
                return Response({'respuesta':True,'mensaje':'registro exitoso'})
            except:
                return Response({'respuesta':False,'mensaje':'registro fallido'})
            


    def list(self,request):
        respuesta = Response(request.data)
        return respuesta





class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all().order_by('razon_social')
    serializer_class = EmpresaSerializer

   

class UsuarioEmpresaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UsuarioEmpresa.objects.all()
    serializer_class = UsuarioEmpresaSerializer
    permission_classes = None

         



class EmpleadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
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

class HerramientaEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = HerramientaEmpleado.objects.all()
    serializer_class = HerramientaEmpleadoSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermisoGrupoViewSet(viewsets.ModelViewSet):
    queryset = PermisoGrupo.objects.all()
    serializer_class = PermisoGrupoSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermisoEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = PermisoEmpleado.objects.all()
    serializer_class = PermisoEmpleadoSerializer
    permission_classes = [permissions.IsAuthenticated]

class SesionEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = SesionEmpleado.objects.all()
    serializer_class = SesionEmpleadoSerializer
    permission_classes = [permissions.IsAdminUser]

class SesionUsuarioViewSet(viewsets.ModelViewSet):
    queryset = SesionUsuario.objects.all()
    serializer_class = SesionUsuarioSerializer
    permission_classes = [permissions.IsAdminUser]