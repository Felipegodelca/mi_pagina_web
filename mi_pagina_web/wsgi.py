"""
WSGI config for mi_pagina_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# 🛠️ Leer el entorno actual (desarrollo o producción)
DJANGO_ENV = os.getenv('DJANGO_ENV', 'production')  # 'production' es el valor predeterminado

if DJANGO_ENV == 'development':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_pagina_web.settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_pagina_web.settings.production')

# 🚀 Inicializar la aplicación WSGI
application = get_wsgi_application()