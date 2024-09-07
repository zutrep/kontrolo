from rest_framework import permissions, viewsets

from portafolio.serializers import *

class TipoClienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoCliente.objects.all()
    serializer_class = TipoClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
