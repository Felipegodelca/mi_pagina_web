from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from articulos import views
from articulos.views import CustomLoginView, debug_headers

# ==========================
# 🛠️ URLs PRINCIPALES
# ==========================
urlpatterns = [
    # Administración
    path('admin/', admin.site.urls, name='admin'),

    # Página de inicio
    path('', views.inicio, name='inicio'),

    # Artículos (rutas traducibles)
    path(_('articulos/'), include('articulos.urls')),

    # Cambio de idioma
    path(_('cambiar_idioma/<str:idioma>/'), views.cambiar_idioma, name='cambiar_idioma'),

    # Autenticación
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/registro/', views.registro, name='registro'),

    # Depuración
    path('debug/headers/', debug_headers, name='debug_headers'),
]

# ==========================
# 🛡️ MANEJO DE ARCHIVOS ESTÁTICOS Y MEDIA
# ==========================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# ==========================
# 🔑 AUTENTICACIÓN PREDETERMINADA
# ==========================
if not settings.DEBUG:
    urlpatterns += [
        path('accounts/', include('django.contrib.auth.urls')),
    ]
