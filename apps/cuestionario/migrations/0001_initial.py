# Generated by Django 2.0.13 on 2019-04-08 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codexamen', models.CharField(max_length=10, unique=True)),
                ('nivel', models.CharField(choices=[('P', 'P'), ('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3')], max_length=50)),
                ('fechacreacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Examen_Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.BooleanField(default=False)),
                ('examen', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cuestionario.Examen')),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('es_correcto', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.TextField()),
                ('nivel', models.CharField(blank=True, choices=[('P', 'P'), ('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3')], max_length=50, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cuestionario.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='opcion',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cuestionario.Pregunta'),
        ),
        migrations.AddField(
            model_name='examen_pregunta',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cuestionario.Pregunta'),
        ),
        migrations.AddField(
            model_name='examen',
            name='participante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cuestionario.Participante'),
        ),
    ]
