from dotenv import load_dotenv
from decouple import config
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os
import dj_database_url

# Determinar el entorno (development o production)
DJANGO_ENV = os.getenv('DJANGO_ENV', 'development').lower()
if DJANGO_ENV == 'production':
    load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env.production')
else:
    load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env.development')

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET KEY
SECRET_KEY = config('DJANGO_SECRET_KEY', default='fallback-secret-key')

# Debug Mode
DEBUG = config('DEBUG', default=True, cast=bool)

# Allowed Hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Application definition 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',  # Funcionalidades específicas de PostgreSQL
    'articulos',  # Tu aplicación personalizada
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mi_pagina_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Directorio para plantillas personalizadas
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

WSGI_APPLICATION = 'mi_pagina_web.wsgi.application'

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', cast=str)
    )
}

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'es'  # Idioma en español
TIME_ZONE = 'America/Mexico_City'  # Zona horaria de México
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Directorios para archivos estáticos personalizados
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directorio para archivos estáticos en producción

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración adicional de cookies
CSRF_COOKIE_SECURE = DJANGO_ENV == 'production'
SESSION_COOKIE_SECURE = DJANGO_ENV == 'production'

# Configuración adicional
SECURE_SSL_REDIRECT = DJANGO_ENV == 'production'
SECURE_HSTS_SECONDS = 31536000 if DJANGO_ENV == 'production' else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = DJANGO_ENV == 'production'
SECURE_HSTS_PRELOAD = DJANGO_ENV == 'production'