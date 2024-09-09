from rest_framework import permissions
from login.models import Usuario, SesionUsuario
from rest_framework.response import Response
from jose import jws
import base64


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
        try:
            sesion = SesionUsuario.objects.get(token=token)
        except:
            return False
        usuario = Usuario.objects.get(id=sesion.usuario_id)
        return usuario
    
    
class IsConectedUsuario():

    def autenticar(usuario=None):
        sesion = None
        try:
            sesion = SesionUsuario.objects.get(usuario_id = usuario.id)
        except:
            return False
        
        if sesion:
            return True


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
            return False



    




   