from django.apps import AppConfig

class ArticulosConfig(AppConfig):
    # Definimos un campo auto incremental para las claves primarias de los modelos
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nombre de la aplicación, que debe coincidir con el nombre del directorio de la app
    name = 'articulos'

    def ready(self):
        # Importamos el archivo de señales (signals.py) cuando se inicie la aplicación
        try:
            import articulos.signals
        except ImportError:
            # Si no se puede importar, registrar un mensaje de error
            raise ImportError("No se pudo importar el archivo de señales 'signals.py' en la aplicación 'articulos'. Asegúrate de que el archivo exista.")