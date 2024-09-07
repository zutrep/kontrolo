from rest_framework import permissions, viewsets

from proveedores.serializers import *

class TipoProveedorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoProveedor.objects.all()
    serializer_class = TipoProveedorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProveedorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [permissions.IsAuthenticated]

