from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import views as auth_views
from articulos import views
from articulos.views import CustomLoginView

urlpatterns = [
    # Administración
    path('admin/', admin.site.urls),

    # Página de inicio
    path('', views.inicio, name='inicio'),

    # Artículos (rutas traducibles)
    path(_('articulos/'), views.lista_articulos, name='lista_articulos'),
    path(_('articulos/crear/'), views.crear_articulo, name='crear_articulo'),
    path(_('articulos/editar/<int:pk>/'), views.editar_articulo, name='editar_articulo'),
    path(_('articulos/eliminar/<int:pk>/'), views.eliminar_articulo, name='eliminar_articulo'),
    path(_('articulos/detalle/<int:pk>/'), views.detalle_articulo, name='detalle_articulo'),

    # Cambio de idioma
    path(_('cambiar_idioma/<str:idioma>/'), views.cambiar_idioma, name='cambiar_idioma'),

    # Autenticación
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Vista personalizada de inicio de sesión
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Cierre de sesión
    path('registro/', views.registro, name='registro'),  # Registro de usuarios
]

# Archivos estáticos y multimedia (en desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])