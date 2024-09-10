from rest_framework import permissions
from login.models import *
from rest_framework.response import Response
from jose import jws
import base64



class GeneraSesionEmpleado():
    def getSesion(token, usuario):
        existe_sesion = None
        try:
            existe_sesion = SesionEmpleado.objects.get(token = token)
        except:
            pass

        if existe_sesion:
            existe_sesion.delete()
            sesion = SesionEmpleado(token=token,empleado_id=usuario.id)
            sesion.save()
        
        else:
            sesion = SesionEmpleado(token=token,empleado_id=usuario.id)
            sesion.save()
        
class GeneraSesion():
    def getSesion(token, usuario):
        existe_sesion = None
        try:
            existe_sesion = SesionUsuario.objects.get(token = token)
        except:
            pass

        if existe_sesion:
            existe_sesion.delete()
            sesion = SesionUsuario(token=token,usuario_id=usuario.id)
            sesion.save()
        
        else:
            sesion = SesionUsuario(token=token,usuario_id=usuario.id)
            sesion.save()
        

class GeneraToken():
    def getToken(request):
        key = str(request.META['REMOTE_ADDR'])
        claim = base64.b64encode(bytes(key.encode('utf-8')))
        token = jws.sign(claim, key, algorithm='HS256')
        return token
              
class Owner():
    def getOwner(request):
        token = GeneraToken.getToken(request=request)
        sesion = None
        usuario = None
        empresa = None
        try:
            sesion = SesionUsuario.objects.get(token=token)

            usuario = Usuario.objects.get(id=sesion.usuario_id)

        except:
            sesion = SesionEmpleado.objects.get(token=token)
            empleado = Empleado.objects.get(id=sesion.empleado)

            empresa = Empresa.objects.get(id=empleado.empresa)
            usuario = Usuario.objects.get(id=empresa.usuario)


        
        if sesion and usuario:
            return usuario
        else:
            return False
    
    
class IsConectedUsuario():

    def autenticar(usuario=None):
        sesion = None
        try:
            sesion = SesionUsuario.objects.get(usuario_id = usuario.id)
        except:
            return False
        
        if sesion:
            return True

class CrudPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):


        if request.method in permissions.SAFE_METHODS:
            return True
        else:

            return False

class Autenticado(permissions.BasePermission):

    def has_permission(self,request,view):
       
        token = GeneraToken.getToken(request)
        sesion = None
        try:
            sesion = SesionUsuario.objects.get(token= token)
        except:
            pass
            
        if sesion:
            return True
        else:            
            autenticado = permissions.IsAdminUser.has_permission(self,request,view)    
           
            return autenticado

class EsEmpleado(permissions.BasePermission):

    def has_permission(self,request,view):

        token = GeneraToken.getToken(request)
        sesion = None
        try:
            sesion = SesionEmpleado.objects.get(token= token)
        except:
            pass
            
        if sesion:
            admitido = None
            try:

                empleado = Empleado.objects.get(id=sesion.empleado_id)
                herramienta = Herramienta.objects.get(nombre=view.herramienta)
                admitido = HerramientaGrupo.objects.filter(herramienta=herramienta.id, grupo=empleado.grupo_id)
            except:
                return False
            
            if admitido:
                return True
            else:
                return False
        else:
            autenticado = Autenticado.has_permission(self,request=request,view=view)    
            return autenticado
        

        
    def has_object_permission(self, request, view, obj):


        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            #el objeto tiene un usuario como owner
            #buscar el usuario o empleado que hace el request con su respectivo token
            token = GeneraToken.getToken(request)
            #print(request.user)
            return True





    




   