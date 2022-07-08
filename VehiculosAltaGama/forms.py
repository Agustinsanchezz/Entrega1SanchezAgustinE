from django import forms

class SedanFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    color = forms.CharField(max_length=20)
    anio = forms.IntegerField()
    precio = forms.IntegerField()
    
    
class CamionetaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    color = forms.CharField(max_length=20)
    anio = forms.IntegerField()
    precio = forms.IntegerField()
    
    
    
    
class DeportivoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    color = forms.CharField(max_length=20)
    anio = forms.IntegerField()
    precio = forms.IntegerField()
    
    
    