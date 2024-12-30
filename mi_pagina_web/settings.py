import os
from pathlib import Path
import environ

# ==========================
# 📁 BASE DIRECTORY
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# 🔑 INICIALIZAR ENVIRON
# ==========================
env = environ.Env(
    DEBUG=(bool, False)  # En producción: False
)

# Leer el archivo .env.consolidado
environ.Env.read_env(os.path.join(BASE_DIR, '.env.consolidado'))

# ==========================
# 🔒 CONFIGURACIÓN DE SEGURIDAD
# ==========================
SECRET_KEY = env('DJANGO_SECRET_KEY', default='fallback-secret-key')
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[
    '127.0.0.1',
    'localhost',
    'kafekean.vercel.app',
    'www.kafekean.vercel.app',
    'kafekean.com',
    'www.kafekean.com'
])

# ==========================
# 🛠️ CONFIGURACIÓN DE LA BASE DE DATOS (SQLite Temporal)
# ==========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==========================
# 📧 CONFIGURACIÓN DE CORREO ELECTRÓNICO (Zoho Mail)
# ==========================
EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = env('EMAIL_HOST', default='smtp.zoho.com')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL', default=False)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='felipegodelca@kafekean.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')

# ==========================
# 🔐 SEGURIDAD
# ==========================
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=True)
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=True)
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=True)
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', default=31536000)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True)
SECURE_HSTS_PRELOAD = env.bool('SECURE_HSTS_PRELOAD', default=True)

# ==========================
# 🛡️ CSRF Trusted Origins
# ==========================
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[
    'https://kafekean.vercel.app',
    'https://www.kafekean.vercel.app',
    'https://kafekean.com',
    'https://www.kafekean.com'
])

# ==========================
# 🛠️ CONFIGURACIÓN DE PLANTILLAS
# ==========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# ==========================
# 🗂️ ARCHIVOS ESTÁTICOS Y MEDIOS
# ==========================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ==========================
# 🚀 APLICACIONES INSTALADAS
# ==========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articulos',  # Tu aplicación personalizada
]

# ==========================
# 🛡️ MIDDLEWARE
# ==========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==========================
# 🌎 INTERNACIONALIZACIÓN
# ==========================
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ==========================
# ✅ CONFIGURACIÓN ADICIONAL
# ==========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==========================
# 🚀 WSGI
# ==========================
WSGI_APPLICATION = 'mi_pagina_web.wsgi.application'