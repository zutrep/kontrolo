from rest_framework import permissions, viewsets
from contabilidad.serializers import *

class ImpuestoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Impuesto.objects.all()
    serializer_class = ImpuestoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImpuestoProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ImpuestoProducto.objects.all()
    serializer_class = ImpuestoProductoSerializer
    permission_classes = [permissions.IsAuthenticated]


