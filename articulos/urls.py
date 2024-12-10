from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

# Nombre del espacio de nombres para evitar conflictos entre aplicaciones
app_name = 'articulos'

urlpatterns = [
    # Página principal: Lista de artículos
    path('', views.lista_articulos, name='lista_articulos'),

    # Detalles de un artículo (se espera un parámetro 'pk')
    path('<int:pk>/', views.detalle_articulo, name='detalle_articulo'),

    # Crear un nuevo artículo (ruta traducible)
    path(_('crear/'), views.crear_articulo, name='crear_articulo'),

    # Editar un artículo (se espera un parámetro 'pk')
    path('<int:pk>/editar/', views.editar_articulo, name='editar_articulo'),

    # Eliminar un artículo (se espera un parámetro 'pk')
    path('<int:pk>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),

    # Registro de usuario
    path(_('registro/'), views.registro, name='registro'),

    # Inicio de sesión (vista personalizada)
    path(_('login/'), views.CustomLoginView.as_view(), name='login'),

    # Cierre de sesión (vista personalizada con plantilla)
    path(_('logout/'), views.logout_view, name='logout'),

    # Tipos de cambio
    path(_('tipos_cambio/'), views.tipos_cambio, name='tipos_cambio'),
]