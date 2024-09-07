from rest_framework import permissions, viewsets
from compras.serializers import *

class BoletaCompraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BoletaCompra.objects.all()
    serializer_class = BoletaCompraSerializer
    permission_classes = [permissions.IsAuthenticated]

class BoletaCompraDetalleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BoletaCompraDetalle.objects.all()
    serializer_class = BoletaCompraDetalleSerializer
    permission_classes = [permissions.IsAuthenticated]

class FacturaCompraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FacturaCompra.objects.all()
    serializer_class = FacturaCompraSerializer
    permission_classes = [permissions.IsAuthenticated]

class FacturaCompraDetalleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FacturaCompraDetalle.objects.all()
    serializer_class = FacturaCompraDetalleSerializer
    permission_classes = [permissions.IsAuthenticated]

