from django.contrib import admin

# Register your models here.
from apps.cuestionario.models import Categoria, Nivel, Pregunta, Opcion, Participante, ExamenPregunta, Puntaje, Examen

class PuntajeModelAdmin(admin.ModelAdmin):

    #fields = ('') # campos q aparece en create y edit
    list_display = ('id', 'nivel', 'categoria', 'puntaje') # campos en la tabla
    search_fields = ('categoria__nombre', ) # campos por los q buscara
    list_filter = ('puntaje', 'nivel', 'categoria') # campos para filtar en la lista

admin.site.register(Categoria)
admin.site.register(Nivel)
admin.site.register(Pregunta)
admin.site.register(Opcion)
admin.site.register(Participante)
admin.site.register(Examen)
admin.site.register(ExamenPregunta)
admin.site.register(Puntaje, PuntajeModelAdmin)