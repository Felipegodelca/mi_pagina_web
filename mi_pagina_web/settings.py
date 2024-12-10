from dotenv import load_dotenv
from decouple import config
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os
import dj_database_url

# Determinar el entorno (development o production)
DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')
if DJANGO_ENV == 'production':
    load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env.production')
else:
    load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env.development')

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = config('DJANGO_SECRET_KEY', default='default-secret-key')
if SECRET_KEY == 'default-secret-key':
    raise ValueError("La variable DJANGO_SECRET_KEY no está configurada en el .env")

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
if not ALLOWED_HOSTS or ALLOWED_HOSTS == ['']:
    raise ValueError("La variable ALLOWED_HOSTS no está configurada en el .env")

# Installed Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articulos',  # Tu aplicación personalizada
    'django.contrib.humanize',  # Para mejorar la presentación de datos
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Correctamente en Middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL Configuration
ROOT_URLCONF = 'mi_pagina_web.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Añadido para incluir directorios de plantillas
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'mi_pagina_web.wsgi.application'

# Database (Usar la URL de base de datos de Render en producción)
DATABASES = {
    'default': dj_database_url.config(
        default=config(
            'DATABASE_URL', 
            default='postgresql://kafekean_db_user:gXGzJdCgvZD4qEQp7rm2iX38dP5fMLXA@dpg-ct9t40jtq21c73bsotn0-a.oregon-postgres.render.com/kafekean_db'
        )
    )
}

# Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization
LANGUAGE_CODE = 'es'  # Cambio de idioma predeterminado a español
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Idiomas disponibles
LANGUAGES = [
    ('es', _('Español')),
    ('en', _('English')),
    ('de', _('Deutsch')),
]

# Carpeta para archivos de traducción
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Static Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CSRF and Cookie Security
# En desarrollo, no usar cookies seguras, ya que no se usa HTTPS
CSRF_COOKIE_SECURE = DJANGO_ENV == 'production'
SESSION_COOKIE_SECURE = DJANGO_ENV == 'production'

# Configuración de Orígenes de CSRF seguros para Render
CSRF_TRUSTED_ORIGINS = [
    'https://kafe-kean.onrender.com',
    'https://www.kafekean.com',  # Añadir tu dominio personalizado si es necesario
]

# HSTS (HTTP Strict Transport Security) solo en producción
if DJANGO_ENV == 'production':
    SECURE_HSTS_SECONDS = 31536000  # 1 año
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
else:
    # Desactivar redirección a HTTPS en desarrollo
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
    SECURE_SSL_REDIRECT = False

# Configuración de redirección después de login y logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG' if DEBUG else 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG else 'ERROR',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'ERROR',
            'propagate': True,
        },
    },
}

# Configuración para supervisión de archivos
USE_WATCHMAN = False

# Configuración para asegurar que Render use HTTPS para los encabezados
if DJANGO_ENV == 'production':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')