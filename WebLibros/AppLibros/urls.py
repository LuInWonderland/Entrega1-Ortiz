from django.urls import path
from AppLibros import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cienciaFiccion', views.cienciaFiccion, name="CienciaFiccion"),
    path('terror', views.terror, name="Terror"),
    path('distopia', views.distopia, name="Distopia"),
    path('fantasia', views.fantasia, name="Fantasia"),
]