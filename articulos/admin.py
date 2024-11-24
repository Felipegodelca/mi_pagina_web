from django.contrib import admin
from .models import Articulo
from django.utils.translation import gettext_lazy as _

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    # Campos visibles en la lista de artículos
    list_display = ('titulo', 'tema', 'fecha_publicacion')  
    # Campos por los que se puede buscar
    search_fields = ('titulo', 'contenido', 'etiquetas')  
    # Filtros laterales para mejorar la navegación
    list_filter = ('tema', 'fecha_publicacion')  
    # Orden de los artículos en la lista
    ordering = ('-fecha_publicacion',)  

    # Configuración de los grupos de campos en el formulario de administración
    fieldsets = (
        (_("Información del Artículo"), {  
            'fields': ('titulo', 'contenido', 'tema', 'etiquetas', 'imagen')
        }),
        (_("Fechas"), {  
            'fields': ('fecha_publicacion',),
        }),
    )

    # Campos de solo lectura
    readonly_fields = ('fecha_publicacion',)  

    # Configuración de acciones personalizadas en el admin
    actions = ['marcar_como_filosofia', 'marcar_como_psicologia', 'marcar_como_negocios']

    def marcar_como_filosofia(self, request, queryset):
        queryset.update(tema='FIL')
        self.message_user(request, _("Los artículos seleccionados fueron marcados como Filosofía."))
    marcar_como_filosofia.short_description = _("Marcar como Filosofía")

    def marcar_como_psicologia(self, request, queryset):
        queryset.update(tema='PSI')
        self.message_user(request, _("Los artículos seleccionados fueron marcados como Psicología."))
    marcar_como_psicologia.short_description = _("Marcar como Psicología")

    def marcar_como_negocios(self, request, queryset):
        queryset.update(tema='NEG')
        self.message_user(request, _("Los artículos seleccionados fueron marcados como Negocios."))
    marcar_como_negocios.short_description = _("Marcar como Negocios")