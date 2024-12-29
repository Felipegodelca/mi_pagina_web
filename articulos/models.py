from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Articulo(models.Model):
    # Opciones para el campo de tema
    TEMA_OPCIONES = [
        ('FIL', _('Filosofía')),
        ('PSI', _('Psicología')),
        ('NEG', _('Negocios')),
    ]

    # Campos del modelo
    titulo = models.CharField(
        max_length=200,
        verbose_name=_("Título"),
        help_text=_("Introduce un título descriptivo para el artículo (máximo 200 caracteres)."),
    )
    contenido = models.TextField(
        verbose_name=_("Contenido"),
        help_text=_("Escribe el contenido completo del artículo aquí."),
    )
    fecha_publicacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Fecha de publicación"),
    )
    tema = models.CharField(
        max_length=3,
        choices=TEMA_OPCIONES,
        default='FIL',
        verbose_name=_("Tema"),
    )
    etiquetas = models.CharField(
        max_length=200,
        help_text=_("Etiquetas separadas por comas, ej: reflexión, conciencia."),
        blank=True,  # Opcional
        null=True,  # Permite valores nulos en la base de datos
        verbose_name=_("Etiquetas"),
    )
    imagen = models.ImageField(
        upload_to='imagenes_articulos/',  # Asegúrate de configurar correctamente los medios en settings.py
        blank=True,  # Opcional
        null=True,
        verbose_name=_("Imagen"),
    )
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Métodos adicionales
    def clean(self):
        """
        Validación personalizada para asegurar que el título tenga al menos 5 caracteres.
        """
        if len(self.titulo) < 5:
            raise ValidationError(_('El título debe tener al menos 5 caracteres.'))

    # Configuración de metadatos
    class Meta:
        verbose_name = _("Artículo")
        verbose_name_plural = _("Artículos")
        ordering = ['-fecha_publicacion']  # Ordena por fecha de publicación descendente

    # Representación en texto
    def __str__(self):
        return self.titulo

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferencias = models.TextField(blank=True, null=True)  # Por ejemplo, preferencias de usuario

    def __str__(self):
        return f"Perfil de {self.user.username}"