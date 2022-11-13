from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse('inicio')

def cienciaFiccion(request):
    return HttpResponse('ciencia ficcion')

def terror(request):
    return HttpResponse('terror')

def distopia(request):
    return HttpResponse('distopia')

def fantasia(request):
    return HttpResponse('fantasia')
