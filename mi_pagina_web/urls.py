from django.contrib import admin
from django.urls import path
from articulos import views  # Importar las vistas de la app articulos
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _  # Para traducciones de rutas

urlpatterns = [
    # Ruta para el panel de administración
    path('admin/', admin.site.urls),

    # Ruta para la página de inicio
    path('', views.inicio, name='inicio'),

    # Rutas traducibles para las vistas principales
    path(_('articulos/'), views.lista_articulos, name='lista_articulos'),  # Lista de artículos
    path(_('articulos/crear/'), views.crear_articulo, name='crear_articulo'),  # Crear artículo
    path(_('articulos/editar/<int:pk>/'), views.editar_articulo, name='editar_articulo'),  # Editar artículo
    path(_('articulos/eliminar/<int:pk>/'), views.eliminar_articulo, name='eliminar_articulo'),  # Eliminar artículo
    path(_('articulos/detalle/<int:pk>/'), views.detalle_articulo, name='detalle_articulo'),  # Detalle del artículo

    # Ruta para cambiar el idioma
    path(_('cambiar_idioma/<str:idioma>/'), views.cambiar_idioma, name='cambiar_idioma'),
]

# Configuración para servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)