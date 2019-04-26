from django.contrib import admin

# Register your models here.
from apps.cuestionario.models import Categoria, Nivel, Pregunta, Opcion, Participante, ExamenPregunta, Puntaje, Examen

admin.site.register(Categoria)
admin.site.register(Nivel)

admin.site.register(Pregunta)
admin.site.register(Opcion)

admin.site.register(Participante)
admin.site.register(Examen)

admin.site.register(ExamenPregunta)
admin.site.register(Puntaje)