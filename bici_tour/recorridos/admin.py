from django.contrib import admin
from .models import Recorrido, Preinscripcion, PuntosMapa

# ----------------------
# Recorridos
# ----------------------

class PuntoMapaInline(admin.TabularInline):
    model = PuntosMapa   # ✅ modelo correcto
    extra = 2
    min_num = 2
    max_num = 2
    template = "admin/edit_inline/tabular.html"

    class Media:  # ✅ así se integran los assets de Leaflet
        css = {'all': ('https://unpkg.com/leaflet/dist/leaflet.css',)}
        js = ('https://unpkg.com/leaflet/dist/leaflet.js',)

class RecorridoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'fecha',
        'tipo',
        'ciudad',
        'estado',
    )
    list_filter = (
        'tipo',
        'ciudad',
        'estado',
        'fecha',
    )
    search_fields = (
        'nombre',
        'ciudad',
        'estado',
        'descripcion'
    )
    
    fieldsets = (
        ('Información General', {
            'fields': (
                ('nombre', 'tipo'),
                ('fecha', 'hora_inicio'),
                'recorrido_realizado'
            ),
        }),
        ('Ubicación y Ruta', {
            'fields': (
                ('ciudad', 'estado'),
                'punto_inicio',
                'punto_final',
            ),
            'description': 'Detalles de la ubicación del recorrido.'
        }),
        ('Detalles y Costo', {
            'fields': (
                'kilometros',
                'tiempo_estimado',
                'costo',
                'descripcion',
                'fotografia'
            ),
        }),
    )
    inlines = [PuntoMapaInline]
    ordering = ('fecha',)

admin.site.register(Recorrido, RecorridoAdmin)


# ----------------------
# Preinscripciones
# ----------------------
@admin.register(Preinscripcion)
class PreinscripcionAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 'correo', 'telefono',
        'ciudad', 'estado', 'recorrido', 'created'
    )
    search_fields = ('nombre', 'correo', 'telefono', 'ciudad', 'estado')
    list_filter = ('recorrido', 'estado', 'ciudad')
    ordering = ('-created',)
    date_hierarchy = 'created'
    list_per_page = 10


# ----------------------
# Rutas y Puntos de Ruta
# ----------------------





# ----------------------
# Mapas
# ----------------------

