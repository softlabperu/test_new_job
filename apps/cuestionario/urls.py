from django.urls import path

from .views import crear_examen, registrar_examen, listar_examen, registra_opcion, formulario, validar_codigo

urlpatterns = [


    # vista para mostrar el ingreso de los datos para crear el examen
    path('CrearExamen/', crear_examen, name="crear_examen"),

    # funcion para registrar y crear a la vez el examen
    path('RegistrarExamen/', registrar_examen, name="registrar_examen"),

    # vista para listar la 1era pregunta del examen
    path('Examen/<str:codexamen>', listar_examen, name="listar_examen"),

    # funcion para el boton sgt del examen
    path('', registra_opcion, name="registra_opcion"),

    # formulario para inggresar al examen
    path('Acceso/', formulario, name="formulario"),

    # funcion para validar el codigo de ingreso
    path('validar', validar_codigo, name="validacodigo"),

]
