import os
from pathlib import Path
import environ
import dj_database_url

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

# 🚀 Modo de depuración (Siempre False en producción)
DEBUG = env.bool('DEBUG', default=False)

# 🌐 Dominios permitidos
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['kafe-kean.onrender.com', 'www.kafe-kean.onrender.com'])

# ==========================
# 🛠️ CONFIGURACIÓN DE LA BASE DE DATOS
# ==========================
DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL')
    )
}

# ==========================
# 📧 CONFIGURACIÓN DE CORREO ELECTRÓNICO
# ==========================
EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = env('EMAIL_HOST', default='smtp.zoho.com')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL', default=False)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='felipegodelca@kafekean.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')

# ==========================
# 🔐 SEGURIDAD DE COOKIES Y CSRF (En Producción: True)
# ==========================
SESSION_COOKIE_SECURE = True  # Cookies solo disponibles vía HTTPS
CSRF_COOKIE_SECURE = True  # CSRF protegido vía HTTPS
SECURE_SSL_REDIRECT = True  # Redirige todo a HTTPS

# ==========================
# 🔐 SEGURIDAD HSTS (En Producción)
# ==========================
SECURE_HSTS_SECONDS = 31536000  # Forzar HTTPS por 1 año
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# ==========================
# 🛡️ CONFIGURACIÓN DE CSRF Trusted Origins
# ==========================
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[
    'https://kafe-kean.onrender.com',
    'https://www.kafe-kean.onrender.com'
])

# ==========================
# 🗂️ CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS
# ==========================
STATIC_URL = '/static/'
# En producción, los archivos estáticos se recopilan en esta carpeta
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Almacenamiento para producción con WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ==========================
# 🖼️ CONFIGURACIÓN DE ARCHIVOS DE MEDIOS
# ==========================
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
    'django.contrib.postgres',  # Funcionalidades específicas de PostgreSQL
    'articulos',  # Tu aplicación personalizada
]

# ==========================
# 🛡️ MIDDLEWARE
# ==========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para archivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==========================
# 🛠️ CONFIGURACIÓN DE URLS Y PLANTILLAS
# ==========================
ROOT_URLCONF = 'mi_pagina_web.urls'

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

WSGI_APPLICATION = 'mi_pagina_web.wsgi.application'

# ==========================
# 🔑 VALIDACIÓN DE CONTRASEÑAS
# ==========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
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
# ✅ ARCHIVOS ESTÁTICOS EN PRODUCCIÓN
# ==========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'