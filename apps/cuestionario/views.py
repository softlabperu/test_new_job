from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy

from apps.cuestionario.models import Pregunta, Opcion, Categoria, Participante, Examen, ExamenPregunta, Nivel, Puntaje

from random import sample
from django.utils.crypto import get_random_string
from django.http import JsonResponse


# Create your views here.

def listar_examen(request, codexamen):
    context = {}
    pregunta = ExamenPregunta.objects.filter(examen__codexamen=codexamen, respuesta_id__isnull=True)
    context['pregunta'] = pregunta.first()
    context['siguiente'] = 'registra_opcion'
    context['ruta_carga'] = reverse_lazy('listar_examen', args=[codexamen])

    return render(request, 'examen.html', context)


def validar_codigo(request):
    context = {}
    if request.method == 'POST':
        codigo = request.POST.get('txtCodigo')
        if codigo != '':
            examen = Examen.objects.get(codexamen=codigo)
            if examen != None:
                context['acceso'] = codigo
                context['salida'] = 2
            else:
                context['salida'] = 1
        else:
            context['salida'] = 0

    return JsonResponse(context, content_type="application/json")


def registra_opcion(request):
    context = {}

    if request.method == 'POST':
        opcion = request.POST.get('respuestas[]')
        if opcion != None:
            idexamen = request.POST.get('txtidexamen')
            examen = ExamenPregunta.objects.get(id=idexamen)
            examen.respuesta_id = opcion
            examen.save()
            context['salida'] = 1
        else:
            context['salida'] = 2
    else:
        context['salida'] = 0

    return JsonResponse(context, content_type="application/json")


def crear_examen(request):
    context = {}
    niveles = Nivel.objects.all()
    context['niveles'] = niveles
    context['crear_examen'] = 'registrar_examen'
    return render(request, 'crear_examen.html', context)


def registrar_examen(request):
    context = {}
    if request.method == 'POST':

        with transaction.atomic():
            # registra los datos del participante}
            documento = request.POST.get('txtdocumento')
            nombres = request.POST.get('txtNombres')
            apellidos = request.POST.get('txtApellidos')
            participante = Participante(nombre=nombres, apellido=apellidos, documento=documento)
            participante.save()

            # registra los datos del examen
            codigo = get_random_string(length=10)
            nivel = request.POST.get('txtnivel')
            examen = Examen(codexamen=codigo, nivel_id=nivel, fechacreacion='', participante_id=participante.id)
            examen.save()

            nivel_seleccionado = Nivel.objects.get(id=nivel)
            niveles = Nivel.objects.filter(orden__lte=nivel_seleccionado.orden).order_by('orden')

            cant_preguntas = 3
            total_ponderado_nivel = sum([n.ponderacion for n in niveles])

            for nivel in niveles:

                porcentaje_nivel = nivel.ponderacion / total_ponderado_nivel

                puntajes = Puntaje.objects.filter(nivel=nivel)

                total_ponderado_categorias_nivel = sum([p.puntaje for p in puntajes])

                for puntaje in puntajes:  # Por cada categoria

                    porcentaje_categoria_nivel = puntaje.puntaje / total_ponderado_categorias_nivel

                    lista_preguntas = list(Pregunta.objects.filter(categoria=puntaje.categoria, nivel=nivel))
                    seleccion_preguntas = sample(lista_preguntas, k=cant_preguntas) if len(lista_preguntas) > 3 else lista_preguntas

                    porcentaje_pregunta_categoria_nivel = 1 / len(seleccion_preguntas)
                    valor_pregunta = porcentaje_nivel * porcentaje_categoria_nivel * porcentaje_pregunta_categoria_nivel

                    for pregunta in seleccion_preguntas:
                        examen_pregunta = ExamenPregunta(examen=examen, pregunta=pregunta, puntaje=valor_pregunta)
                        examen_pregunta.save()

            context['CodeExamen'] = codigo

        context['salida'] = 1

    return JsonResponse(context, content_type="application/json")


def formulario(request):
    context = {}
    context['formulario'] = 'validacodigo'
    return render(request, 'formulario.html', context)
