from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-secret-key')  # Usar variable de entorno
DEBUG = False  # Cambiar a False en producción
LLOWED_HOSTS = ['127.0.0.1', 'localhost', 'kafekean.com', 'www.kafekean.com', 'mi-app.onrender.com']

# Installed Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articulos',  # Tu aplicación personalizada
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Middleware para traducción
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
        'DIRS': [],  # Si tienes plantillas fuera de las apps, agrégalas aquí
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Necesario para las plantillas de autenticación
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'mi_pagina_web.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Para producción, considera usar PostgreSQL o MySQL
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization
LANGUAGE_CODE = 'en'  # Idioma predeterminado
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'  # URL base para archivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Directorio donde están tus archivos estáticos
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Carpeta para recopilar archivos estáticos en producción

# Archivos multimedia
MEDIA_URL = '/media/'  # URL base para archivos multimedia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Carpeta donde se almacenan los archivos multimedia

# Configuración adicional para archivos estáticos
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Idiomas disponibles
LANGUAGES = [
    ('es', _('Español')),
    ('en', _('English')),
    ('de', _('Deutsch')),
]

# Carpeta para archivos de traducción
LOCALE_PATHS = [
    BASE_DIR / 'locale',  # Carpeta donde se guardan archivos .po y .mo
]

# Configuración adicional
CSRF_TRUSTED_ORIGINS = [
    'https://kafekean.com',
    'https://www.kafekean.com',
]

# Configuración de redirección después de login y logout
LOGIN_REDIRECT_URL = '/'  # Redirige a la página de inicio después de iniciar sesión
LOGOUT_REDIRECT_URL = '/'  # Redirige a la página de inicio después de cerrar sesión

# Debugging y otras configuraciones opcionales
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Configuración para supervisión de archivos
USE_WATCHMAN = False