from django.shortcuts import render

from apps.cuestionario.models import Pregunta,Opcion,Categoria,Participante,Examen,Examen_Pregunta

from random import random,sample
from django.utils.crypto import get_random_string
from datetime import datetime

from django.http import JsonResponse

# Create your views here.

def listar_examen(request):
    context = {}
    pre = Pregunta.objects.all()
    alt =  Opcion.objects.all()

    body = []
    alternativas = []
    for datos in pre:
        body.append({'id':datos.id,'pregunta':datos.pregunta})

    for data in alt:
        alternativas.append({'id':data.id,'alternativa':data.texto,'idpregunta':data.pregunta_id})

    context['preguntas'] = body
    context['alternativas'] = alternativas

    return render(request,'examen.html',context)


def registrar(request):
    context = {}
    context['crear_examen'] = 'crear_examen'
    return render(request,'crear_examen.html',context)



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
            cuestionario = Examen_Pregunta(examen_id=examen.id, pregunta_id=p.id)
            cuestionario.save()

        context['salida'] = 1
    return JsonResponse(context, content_type="application/json")
