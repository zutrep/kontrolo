from rest_framework import permissions, viewsets
from logistica.serializers import *

class SedeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
    permission_classes = [permissions.IsAuthenticated]

class AlmacenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer
    permission_classes = [permissions.IsAuthenticated]

class UnidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

class InventarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class IngresoInventarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IngresoInventario.objects.all()
    serializer_class = IngresoInventarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class SalidaInventarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SalidaInventario.objects.all()
    serializer_class = SalidaInventarioSerializer
    permission_classes = [permissions.IsAuthenticated]

