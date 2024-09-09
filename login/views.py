from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from login import permisos
from login.models import Usuario, SesionUsuario
from rest_framework.response import Response
from django.utils import timezone
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



class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('email')
    serializer_class = UsuarioSerializer
    #permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        action = self.action
        if action == 'destroy' or action == 'list' or action == 'partial_update':
            permission_classes = [permissions.IsAdminUser]
        elif action == 'update':
            permission_classes = [permisos.Autenticado]
        else:
            permission_classes = [permissions.AllowAny]
                    
        return [permission() for permission in permission_classes]
        
    def retrieve(self,request, pk=None):
        usuario = None
        try:
            usuario = Usuario.objects.get(id=pk)
        except:
            return Response({'respuesta':False, 'mensaje':'no existe el usuario'})
        
        if usuario:
            conectado = None
            try:
                conectado = permisos.IsConectedUsuario.autenticar(usuario=usuario)
            except:
                pass
            
            
            if conectado:
                token = permisos.GeneraToken.getToken(request)
                sesion = SesionUsuario.objects.get(token = token)
                if sesion.usuario_id == pk:

                    data = {
                        'id':usuario.id,
                        'nombre':usuario.nombre,
                        'email':usuario.email,
                    }
                    return Response(data)
            else:
                return Response({'respuesta':False, 'mensaje':'No se han proveido las credenciales'})
        else:
            return Response({'respuesta':False, 'mensaje':'No se han proveido las credenciale'})




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
                
                token = permisos.GeneraToken.getToken(request)
              
                #generar sesion de ususario
                permisos.GeneraSesion.getSesion(token, usuario)

                return Response({'respuesta':True,'mensaje':'login exitoso','token':token})
            else:
                return Response({'respuesta':False,'mensaje':'usuario o password incorrectos'})
        else:
            try:
                usuario = Usuario(nombre=nombre,email=email,password=password)
                usuario.save()
                return Response({'respuesta':True,'mensaje':'registro exitoso'})
            except:
                return Response({'respuesta':False,'mensaje':'registro fallido'})
            
    def update(self,request,pk=None):
        try:
            usuario = Usuario.objects.get(id=request.data['id'])
            usuario.password = request.data['password']
            usuario.nombre = request.data['nombre']
            usuario.save()
        except:
            return Response({'respuesta':False,'mensaje':'Error algo salio mal'})

        return Response({'respuesta':True,'mensaje':'edicion exitosa'})

    
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all().order_by('razon_social')
    serializer_class = EmpresaSerializer
    permission_classes = [permisos.Autenticado]

    def create(self,request):
        owner = permisos.Owner.getOwner(request)
        empresa = Empresa(
            razon_social=request.data['razon_social'],
            registro=request.data['registro'],
            direccion=request.data['direccion'],
            usuario_id= owner.id
        )
        empresa.save()
        if empresa:
            return Response({'respuesta':True,'mensaje':'Empresa creada exitosamente'})
        else:
            return Response({'respuesta':False,'mensaje':'No se ha podido crear la empresa'})

    
    def list(self,request):
        owner = permisos.Owner.getOwner(request)
        empresas = [{
            'razon_social':empresa.razon_social,
            'registro':empresa.registro,
            'direccion':empresa.direccion,
            'fecha_creacion': empresa.fecha_creacion
                     } for empresa in Empresa.objects.filter(usuario_id=owner, estado=1)]
        return Response(empresas)
    
    def retrieve(self,request,pk=None):
        owner = permisos.Owner.getOwner(request)

        data = [{
            'id':empresa.id,
            'razon_social':empresa.razon_social,
            'registro':empresa.registro,
            'direccion':empresa.direccion,
            'fecha_creacion': empresa.fecha_creacion
                     } for empresa in Empresa.objects.filter(id=pk,usuario_id=owner.id)]
        return Response(data)

    def update(self,request,pk=None):
        owner = permisos.Owner.getOwner(request)
        try:
            empresa = Empresa.objects.get(id=request.data['id'], usuario_id = owner.id, estado = 1)
            empresa.razon_social = request.data['razon_social']
            empresa.registro = request.data['registro']
            empresa.direccion = request.data['direccion']
            empresa.save()
        except:
            return Response({'respuesta':False,'mensaje':'Error algo salio mal'})

        return Response({'respuesta':True,'mensaje':'Empresa creada exitosamente'})
        
    def destroy(self,request,pk=None):
        owner = permisos.Owner.getOwner(request)
        try:
           empresa = Empresa.objects.get(id=request.data['id'], usuario_id = owner.id, estado = 1)
           empresa.estado = 0
           empresa.save()
        except:
           return Response({'respuesta':False,'mensaje':'Error algo salio mal'})

        return Response({'respuesta':True,'mensaje':'Empresa eliminada exitosamente'})
        

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all().order_by('nombre')
    serializer_class = GrupoSerializer
    permission_classes = [permisos.Autenticado]

    def create(self,request):
        owner = permisos.Owner.getOwner(request)
        try:
            grupo = Grupo(
                    usuario=owner.id,
                    nombre=request.data['nombre']
                    )
            grupo.save()
        except:
           return Response({'respuesta':False,'mensaje':'Error algo salio mal'})

        return Response({'respuesta':True,'mensaje':'Grupo creado exitosamente'})
    
    def list(self,request):
        owner = permisos.Owner.getOwner(request)
        try:
            grupos = Grupo.objects.filter(usuario_id = owner.id)
            data = [{'id':grupo.id,'nombre':grupo.nombre, 'usuario':grupo.usuario} for grupo in grupos]
        except:
           return Response({'respuesta':False,'mensaje':'Error algo salio mal'})

        return Response(data)
    
    def retrieve(self, request, pk=None):
        owner = permisos.Owner.getOwner(request)
        try:
            grupos = Grupo.objects.filter(usuario_id = owner.id, id=pk)
            data = [{'id':grupo.id,'nombre':grupo.nombre, 'usuario':grupo.usuario} for grupo in grupos]
        except:
           return Response({'respuesta':False,'mensaje':'Error algo salio mal'})

        return Response(data)
    
    def update(self,request,pk=None):
        owner = permisos.Owner.getOwner(request)
        try:
            grupo = Grupo.objects.get(usuario_id = owner.id, id=pk)
            grupo.nombre = request.data['nombre']
            grupo.save()
        except:
           return Response({'respuesta':False,'mensaje':'Error algo salio mal'})

        return Response({'respuesta':True,'mensaje':'Se actualizaron correctamente los datos'})
    
    def destroy(self,request,pk=None):
        owner = permisos.Owner.getOwner(request)
        try:
            grupo = Grupo.objects.get(usuario_id = owner.id, id=pk)
            grupo.estado = 0
            grupo.save()
        except:
           return Response({'respuesta':False,'mensaje':'Error algo salio mal'})
        
        return Response({'respuesta':True,'mensaje':'Se Elimino correctamente el grupo'})
    


class EmpleadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
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