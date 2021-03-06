from django.db import models, transaction

# Create your models here.
NIVELES = (
    ("P", "P"),
    ("P1", "P1"),
    ("P2", "P2"),
    ("P3", "P3")
)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre


class Nivel(models.Model):
    nombre = models.CharField(max_length=10, null=False, blank=False)
    orden = models.IntegerField(null=True, blank=False)
    ponderacion = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    pregunta = models.TextField(null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=False, blank=False)
    nivel = models.ForeignKey(Nivel, on_delete=models.DO_NOTHING, null=True, blank=False)
    #nivel = models.CharField(max_length=50, choices=NIVELES, null=True, blank=True)

    def __str__(self):
        return self.pregunta[:100]

    @property
    def opciones(self):
        return Opcion.objects.filter(pregunta=self)



class Opcion(models.Model):
    texto = models.TextField(null=False, blank=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.DO_NOTHING, null=False, blank=False)
    es_correcto = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.texto



class Participante(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    documento = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.apellido, self.documento)



class Examen(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.DO_NOTHING, null=False, blank=False)
    codexamen = models.CharField(max_length=10, null=False, blank=False, unique=True)
    nivel = models.ForeignKey(Nivel, on_delete=models.DO_NOTHING, null=True, blank=False)
    fechacreacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.participante, self.codexamen)



class ExamenPregunta(models.Model):

    class Meta:
        db_table = 'cuestionario_examen_pregunta'

    examen = models.ForeignKey(Examen, on_delete=models.DO_NOTHING, null=False, blank=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.DO_NOTHING, null=False, blank=False)
    respuesta = models.ForeignKey(Opcion, on_delete=models.DO_NOTHING, null=True, blank=False)
    puntaje = models.FloatField(null=True, blank=False)

    def __str__(self):
        return '{} {}'.format(self.examen, self.pregunta)


class Puntaje(models.Model):
    nivel = models.ForeignKey(Nivel, on_delete=models.DO_NOTHING, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=False, blank=False)
    puntaje = models.IntegerField(null=False, blank=False)


