from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = 'django-insecure-#gq-webbm)30uepztylc*&m!tp8-(w2916r665nq)djk0rmos6'
DEBUG = True
ALLOWED_HOSTS = ['*']

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
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # Contexto requerido
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Localization
LANGUAGE_CODE = 'es'  # Idioma predeterminado
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'  # URL base para archivos estáticos
STATICFILES_DIRS = [BASE_DIR / 'static']  # Directorios donde Django buscará archivos estáticos
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Carpeta para archivos estáticos recopilados en producción

# Archivos multimedia
MEDIA_URL = '/media/'  # URL base para archivos multimedia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Carpeta donde se almacenan los archivos multimedia

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
    BASE_DIR / 'locale',  # Carpeta para almacenar archivos .po/.mo
]

# Configuración adicional
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000']  # Configuración opcional para hosts confiables

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