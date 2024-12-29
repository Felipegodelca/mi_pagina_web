from django import forms
from .models import Articulo
from django.utils.translation import gettext_lazy as _

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo  # El formulario se basa en el modelo Articulo
        fields = ['titulo', 'contenido', 'tema', 'etiquetas', 'imagen']  # Campos a incluir en el formulario

        # Personalización de widgets para los campos
        widgets = {
            'contenido': forms.Textarea(attrs={
                'rows': 5, 
                'placeholder': _('Escribe el contenido aquí...'),
                'class': 'form-control',  # Agregado para mejorar el estilo del campo
            }),
            'etiquetas': forms.TextInput(attrs={
                'placeholder': _('Etiquetas separadas por comas, ej: reflexión, conciencia'),
                'class': 'form-control',  # Agregado para mejorar el estilo del campo
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',  # Estilo para el campo de archivo de imagen
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
            'etiquetas': _('Usa comas para separar las etiquetas. Ejemplo: filosofía, psicología, negocios.'),
        }

    # Validación personalizada para el título
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 5:
            raise forms.ValidationError(_("El título debe tener al menos 5 caracteres."))
        return titulo

    # Validación personalizada para el contenido
    def clean_contenido(self):
        contenido = self.cleaned_data.get('contenido')
        if len(contenido) < 20:
            raise forms.ValidationError(_("El contenido debe tener al menos 20 caracteres."))
        return contenido