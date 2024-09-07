from rest_framework import permissions, viewsets

from restaurant.serializers import *

class MesaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    permission_classes = [permissions.IsAuthenticated]

class MesaAtencionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MesaAtencion.objects.all()
    serializer_class = MesaAtencionSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlatoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlatoSedeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlatoSede.objects.all()
    serializer_class = PlatoSedeSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecetaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
    permission_classes = [permissions.IsAuthenticated]

