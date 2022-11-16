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
    form = forms.CienciaFiccionForm()
    libros = models.CienciaFiccion.objects.all()
    if request.method == 'POST':
        form = forms.CienciaFiccionForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            libro_ciencia_ficcion = models.CienciaFiccion(titulo = info['titulo'], autor = info['autor'], sinopsis = info['sinopsis'], url_portada = info['url_portada'])
            libro_ciencia_ficcion.save()
    if request.method == 'GET' and 'buscador' in request.GET:
        buscador = request.GET['buscador']
        libros = models.CienciaFiccion.objects.filter(titulo__icontains=buscador).union(models.CienciaFiccion.objects.filter(autor__icontains=buscador))
    return render(request, 'cienciaFiccion.html', {'form': form, 'libros': libros})

def distopia(request):
    form = forms.DistopiaForm()
    libros = models.Distopia.objects.all()
    if request.method == 'POST':
        form = forms.DistopiaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            libro_distopia = models.Distopia(titulo = info['titulo'], autor = info['autor'], sinopsis = info['sinopsis'], url_portada = info['url_portada'])
            libro_distopia.save()
    if request.method == 'GET' and 'buscador' in request.GET:
        buscador = request.GET['buscador']
        libros = models.Distopia.objects.filter(titulo__icontains=buscador).union(models.Distopia.objects.filter(autor__icontains=buscador))
    return render(request, 'distopia.html', {'form': form, 'libros': libros})


def terror(request):
    form = forms.TerrorForm()
    libros = models.Terror.objects.all()
    if request.method == 'POST':
        form = forms.TerrorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            libro_terror = models.Terror(titulo = info['titulo'], autor = info['autor'], sinopsis = info['sinopsis'], url_portada = info['url_portada'])
            libro_terror.save()
    if request.method == 'GET' and 'buscador' in request.GET:
        buscador = request.GET['buscador']
        libros = models.Terror.objects.filter(titulo__icontains=buscador).union(models.Terror.objects.filter(autor__icontains=buscador))
    return render(request, 'terror.html', {'form': form, 'libros': libros})

def fantasia(request):
    form = forms.FantasiaForm()
    libros = models.Fantasia.objects.all()
    if request.method == 'POST':
        form = forms.FantasiaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            libro_fantasia = models.Fantasia(titulo = info['titulo'], autor = info['autor'], sinopsis = info['sinopsis'], url_portada = info['url_portada'])
            libro_fantasia.save()
    if request.method == 'GET' and 'buscador' in request.GET:
        buscador = request.GET['buscador']
        libros = models.Fantasia.objects.filter(titulo__icontains=buscador).union(models.Fantasia.objects.filter(autor__icontains=buscador))
    return render(request, 'fantasia.html', {'form': form, 'libros': libros})