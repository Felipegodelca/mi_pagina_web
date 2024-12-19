from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

# Nombre del espacio de nombres para evitar conflictos entre aplicaciones
app_name = 'articulos'

urlpatterns = [
    # Página principal: Lista de artículos
    path('', views.lista_articulos, name='lista_articulos'),  # Lista de artículos

    # Detalles de un artículo
    path('<int:pk>/', views.detalle_articulo, name='detalle_articulo'),  # Detalle de un artículo

    # Crear un nuevo artículo (ruta traducible)
    path(_('crear/'), views.crear_articulo, name='crear_articulo'),  # Crear artículo

    # Editar un artículo
    path('<int:pk>/editar/', views.editar_articulo, name='editar_articulo'),  # Editar artículo

    # Eliminar un artículo
    path('<int:pk>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),  # Eliminar artículo

    # Registro de usuario
    path(_('registro/'), views.registro, name='registro'),  # Registro de usuario

    # Inicio de sesión
    path(_('login/'), views.CustomLoginView.as_view(), name='login'),  # Login personalizado

    # Cierre de sesión
    path(_('logout/'), views.logout_view, name='logout'),  # Logout personalizado

    # Tipos de cambio
    path(_('tipos_cambio/'), views.tipos_cambio, name='tipos_cambio'),  # Mostrar tipos de cambio
]