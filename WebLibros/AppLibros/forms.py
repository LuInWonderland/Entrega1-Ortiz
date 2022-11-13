from django import forms

class CienciaFiccionForm(forms.Form):
    titulo = forms.CharField()
    autor  = forms.CharField()
    sinopsis = forms.CharField()
    url_portada = forms.CharField()

class TerrorForm(forms.Form):
    titulo = forms.CharField()
    autor  = forms.CharField()
    sinopsis = forms.CharField()
    url_portada = forms.CharField()

class DistopiaForm(forms.Form):
    titulo = forms.CharField()
    autor  = forms.CharField()
    sinopsis = forms.CharField()
    url_portada = forms.CharField()

class FantasiaForm(forms.Form):
    titulo = forms.CharField()
    autor  = forms.CharField()
    sinopsis = forms.CharField()
    url_portada = forms.CharField()

