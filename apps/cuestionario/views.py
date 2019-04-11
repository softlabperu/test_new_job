from django.shortcuts import render
from django.urls import reverse_lazy

from apps.cuestionario.models import Pregunta, Opcion, Categoria, Participante, Examen, ExamenPregunta

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
               context['ruta'] = examen.id
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


def registrar(request):
    context = {}
    context['crear_examen'] = 'crear_examen'
    return render(request, 'crear_examen.html', context)


def crear_examen(request):
    context = {}
    if request.method == 'POST':
        # registra los datos del participante
        documento = request.POST.get('txtdocumento')
        nombres = request.POST.get('txtNombres')
        apellidos = request.POST.get('txtApellidos')
        participante = Participante(nombre=nombres, apellido=apellidos, documento=documento)
        participante.save()

        # registra los datos del examen
        codigo = get_random_string(length=10)
        nivel = request.POST.get('txtnivel')
        examen = Examen(codexamen=codigo, nivel=nivel, fechacreacion='', participante_id=participante.id)
        examen.save()

        # generar las preguntas aleatorias
        preguntas = []
        categorias = Categoria.objects.all()
        for categoria in categorias:
            lista_preguntas = list(Pregunta.objects.filter(categoria=categoria))
            seleccion_preguntas = sample(lista_preguntas, k=3)
            preguntas = preguntas + seleccion_preguntas

        # registrar las preguntas
        for p in preguntas:
            cuestionario = ExamenPregunta(examen_id=examen.id, pregunta_id=p.id)
            cuestionario.save()

        context['salida'] = 1
        context['CodeExamen'] = codigo

    return JsonResponse(context, content_type="application/json")


def formulario(request):
    context = {}
    context['formulario'] = 'validacodigo'
    return render(request, 'formulario.html', context)
