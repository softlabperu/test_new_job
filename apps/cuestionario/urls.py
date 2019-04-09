from django.urls import path

from apps.cuestionario.views import listar_examen,registrar,crear_examen

urlpatterns = [

    path('Examen/',listar_examen, name="listar_examen"),

    path('Registrar/',registrar, name="registrar"),

    path('CrearExamen',crear_examen, name="crear_examen"),

]