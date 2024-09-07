from rest_framework import permissions, viewsets
from ventas.serializers import *

class BoletaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer
    permission_classes = [permissions.IsAuthenticated]

class BoletaDetalleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BoletaDetalle.objects.all()
    serializer_class = BoletaDetalleSerializer
    permission_classes = [permissions.IsAuthenticated]

class FacturaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [permissions.IsAuthenticated]

class FacturaDetalleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FacturaDetalle.objects.all()
    serializer_class = FacturaDetalleSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecetaBoletaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RecetaBoleta.objects.all()
    serializer_class = RecetaBoletaSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecetaBoletaDetalleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RecetaBoletaDetalle.objects.all()
    serializer_class = RecetaBoletaDetalleSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecetaFacturaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RecetaFactura.objects.all()
    serializer_class = RecetaFacturaSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecetaFacturaDetalleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RecetaFacturaDetalle.objects.all()
    serializer_class = RecetaFacturaDetalleSerializer
    permission_classes = [permissions.IsAuthenticated]
