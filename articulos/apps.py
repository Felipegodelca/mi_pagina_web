from django.apps import AppConfig


class ArticulosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articulos'

    def ready(self):
        import articulos.signals  # Registro de señales al cargar la app