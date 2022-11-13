from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppLibros import forms
from AppLibros import models

# Create your views here.
def inicio(request):
    plantilla = loader.get_template('inicio.html')
    contexto = {}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def cienciaFiccion(request):
    plantilla = loader.get_template('cienciaFiccion.html')
    contexto = {}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def terror(request):
    if request.method == 'POST':
        form = forms.TerrorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            libro_terror = models.Terror(titulo = info['titulo'], autor = info['autor'], sinopsis = info['sinopsis'], url_portada = info['url_portada'])
            libro_terror.save()
    form = forms.TerrorForm()
    return render(request, 'terror.html', {'form': form})

def distopia(request):
    plantilla = loader.get_template('distopia.html')
    contexto = {}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def fantasia(request):
    plantilla = loader.get_template('fantasia.html')
    contexto = {}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)