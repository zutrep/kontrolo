from django.urls import include, path
from rest_framework import routers

from login.views import *
from logistica.views import *
from portafolio.views import *
from proveedores.views import *
from restaurant.views import *
from ventas.views import *
from contabilidad.views import *
from compras.views import *

router = routers.DefaultRouter()
#login app
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'Usuario', UsuarioViewSet)
router.register(r'UsuarioEmpresa', UsuarioEmpresaViewSet)
router.register(r'Empleado', EmpleadoViewSet)
router.register(r'Grupo', GrupoViewSet)
router.register(r'Herramienta', HerramientaViewSet)
router.register(r'HerramientaGrupo', HerramientaGrupoViewSet)
router.register(r'HerramientaEmpleado', HerramientaEmpleadoViewSet)
router.register(r'Permiso', PermisoViewSet)
router.register(r'PermisoGrupo', PermisoGrupoViewSet)
router.register(r'PermisoEmpleado', PermisoEmpleadoViewSet)
router.register(r'SesionUsuario', SesionUsuarioViewSet)
router.register(r'SesionEmpleado', SesionEmpleadoViewSet)
#logistica app
router.register(r'Sede', SedeViewSet)
router.register(r'Almacen', AlmacenViewSet)
router.register(r'Unidad', UnidadViewSet)
router.register(r'Producto', ProductoViewSet)
router.register(r'Inventario', InventarioViewSet)
router.register(r'IngresoInventario', IngresoInventarioViewSet)
router.register(r'SalidaInventario', SalidaInventarioViewSet)
#portafolio app
router.register(r'TipoCliente', TipoClienteViewSet)
router.register(r'Cliente', ClienteViewSet)

#proveedores app
router.register(r'TipoProveedor', TipoProveedorViewSet)
router.register(r'Proveedor', ProveedorViewSet)
#restaurant app
router.register(r'Mesa', MesaViewSet)
router.register(r'MesaAtencion', MesaAtencionViewSet)
router.register(r'Plato', PlatoViewSet)
router.register(r'PlatoSede', PlatoSedeViewSet)
router.register(r'Receta', RecetaViewSet)
#ventas app
router.register(r'Boleta', BoletaViewSet)
router.register(r'BoletaDetalle', BoletaDetalleViewSet)
router.register(r'Factura', FacturaViewSet)
router.register(r'FacturaDetalle', FacturaDetalleViewSet)
router.register(r'RecetaBoleta', RecetaBoletaViewSet)
router.register(r'RecetaBoletaDetalle', RecetaBoletaDetalleViewSet)
router.register(r'RecetaFactura', RecetaFacturaViewSet)
router.register(r'RecetaFacturaDetalle', RecetaFacturaDetalleViewSet)
#contabilidad
router.register(r'Impuesto', ImpuestoViewSet)
router.register(r'ImpuestoProducto', ImpuestoProductoViewSet)
#compras
router.register(r'BoletaCompra', BoletaCompraViewSet)
router.register(r'BoletaCompraDetalle', BoletaCompraDetalleViewSet)
router.register(r'FacturaCompra', FacturaCompraViewSet)
router.register(r'FacturaCompraDetalle', FacturaCompraDetalleViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]