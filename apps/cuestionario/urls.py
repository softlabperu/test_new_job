from django.urls import path

from apps.cuestionario.views import listar_examen, registrar, crear_examen, registra_opcion, formulario, validar_codigo

urlpatterns = [

    # vista para listar la 1era pregunta del examen
    #path('Examen/', listar_examen, name="listar_examen"),
    path('Examen/<str:codexamen>', listar_examen, name="listar_examen"),

    # funcion para el boton sgt del examen
    path('', registra_opcion, name="registra_opcion"),

    # vista para mostrar el ingreso de los datos
    path('Registrar/', registrar, name="registrar"),

    # funcion para registrar y crear a la vez el examen
    path('CrearExamen/', crear_examen, name="crear_examen"),

    # formulario para inggresar al examen
    path('Formulario/', formulario, name="formulario"),

    # funcion para validar el codigo de ingreso
    path('validar', validar_codigo, name="validacodigo"),

]
