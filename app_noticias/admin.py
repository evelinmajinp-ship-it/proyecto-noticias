
from django.contrib import admin
from django.utils.html import format_html
from .models import Noticia


class NoticiaAdmin(admin.ModelAdmin):

    # Columnas que aparecerán en el listado
    list_display = (
        'titulo',
        'fecha_ocurrencia',
        'lugar',
        'mostrar_imagen'
    )

    # Filtros disponibles
    list_filter = ('fecha_ocurrencia', 'lugar')

    # Campos en los que se puede buscar
    search_fields = ('titulo', 'lugar', 'descripcion')

    # Ordenar de la noticia más reciente a la más antigua
    ordering = ('-fecha_ocurrencia',)

    # Mostrar 10 noticias por página
    list_per_page = 10

    # Agregar navegación por fechas
    date_hierarchy = 'fecha_ocurrencia'

    # Mostrar una vista previa de la imagen
    @admin.display(description='Imagen')
    def mostrar_imagen(self, obj):

        if obj.imagen:
            return format_html(
                '<img src="{}" width="80" height="55" '
                'style="object-fit: cover; border-radius: 6px;">',
                obj.imagen.url
            )

        return 'Sin imagen'


admin.site.register(Noticia, NoticiaAdmin)

# Personalización del panel administrativo

admin.site.site_header = 'Centro de Automatización Industrial'
admin.site.site_title = 'Administración de Noticias'
admin.site.index_title = 'Panel de gestión de noticias'
