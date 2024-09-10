from rest_framework import permissions, viewsets
from logistica.serializers import *
from login import permisos

class SedeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
    herramienta = "sede"
    permission_classes = [permisos.EsEmpleado]


class AlmacenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer
    permission_classes = [permisos.EsEmpleado]

class UnidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer
    permission_classes = [permisos.EsEmpleado]

class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permisos.EsEmpleado]

class InventarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [permisos.EsEmpleado]

class IngresoInventarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IngresoInventario.objects.all()
    serializer_class = IngresoInventarioSerializer
    permission_classes = [permisos.EsEmpleado]

class SalidaInventarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SalidaInventario.objects.all()
    serializer_class = SalidaInventarioSerializer
    permission_classes = [permisos.EsEmpleado]

