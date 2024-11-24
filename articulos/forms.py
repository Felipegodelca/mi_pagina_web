from django import forms
from .models import Articulo
from django.utils.translation import gettext_lazy as _

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo  # Indica que este formulario se basa en el modelo Articulo
        fields = ['titulo', 'contenido', 'tema', 'etiquetas', 'imagen']  # Incluye el campo de imagen y otros campos necesarios

        # Personalizar widgets para los campos
        widgets = {
            'contenido': forms.Textarea(attrs={
                'rows': 5, 
                'placeholder': _('Escribe el contenido aquí...'),
            }),
            'etiquetas': forms.TextInput(attrs={
                'placeholder': _('Etiquetas separadas por comas, ej: reflexión, conciencia'),
            }),
        }
        labels = {
            'titulo': _('Título'),
            'contenido': _('Contenido'),
            'tema': _('Tema'),
            'etiquetas': _('Etiquetas'),
            'imagen': _('Imagen'),
        }
        help_texts = {
            'etiquetas': _('Usa comas para separar las etiquetas.'),
        }

    # Validación personalizada para el título
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 5:
            raise forms.ValidationError(_("El título debe tener al menos 5 caracteres."))
        return titulo