from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    """
    Crea automáticamente un perfil para cada usuario nuevo.
    """
    if created:
        # Solo se crea un perfil si el usuario es nuevo
        Perfil.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    """
    Guarda automáticamente el perfil cuando se guarda el usuario.
    Esto asegura que cualquier cambio en el usuario también se refleje en el perfil.
    """
    # Verifica si el perfil existe antes de intentar guardarlo
    if hasattr(instance, 'perfil'):
        instance.perfil.save()