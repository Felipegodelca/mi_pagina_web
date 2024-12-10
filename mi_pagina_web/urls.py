from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from articulos import views
from articulos.views import CustomLoginView, debug_headers

urlpatterns = [
    # Administración
    path('admin/', admin.site.urls),  # Ruta para el panel de administración

    # Página de inicio
    path('', views.inicio, name='inicio'),  # Ruta para la página principal de inicio

    # Artículos (rutas traducibles)
    path(_('articulos/'), include('articulos.urls')),  # Incluye las URLs de la app 'articulos'

    # Cambio de idioma
    path(_('cambiar_idioma/<str:idioma>/'), views.cambiar_idioma, name='cambiar_idioma'),

    # Autenticación
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Vista personalizada de inicio de sesión
    path('accounts/logout/', views.logout_view, name='logout'),  # Ruta personalizada para cerrar sesión
    path('accounts/registro/', views.registro, name='registro'),  # Ruta para registrar un nuevo usuario

    # Depuración
    path('debug/headers/', debug_headers, name='debug_headers'),
]

# Archivos estáticos y multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# Rutas adicionales en producción
if not settings.DEBUG:
    urlpatterns += [
        path('accounts/', include('django.contrib.auth.urls')),  # Rutas adicionales para autenticación
    ]
