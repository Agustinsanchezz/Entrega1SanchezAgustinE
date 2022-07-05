from django.shortcuts import render
from django.http import HttpResponse
from VehiculosAltaGama.models import Sedan, Camioneta, Deportivo
from VehiculosAltaGama.forms import *

# Create your views here.
def sport(request):
    auto = Deportivo.objects.all()
    contexto = {'auto': auto}
    return render(request, 'VehiculosAltaGama/sport.html', contexto)
   
def sedan(request):
    auto = Sedan.objects.all()
    contexto = {'auto': auto}
    return render(request, 'VehiculosAltaGama/Sedan.html', contexto)


def camionetas(request):
    auto = Camioneta.objects.all()
    contexto = {'camioneta':auto}
    return render(request, 'VehiculosAltaGama/Camionetas.html', contexto)

def inicio(request):
    return render(request, 'VehiculosAltaGama/inicio.html')



def formularioCamionetas(request):
    if request.method == "POST":
        miFormulario = CamionetaFormulario(request.POST) 
        print(miFormulario)
        
        if CamionetaFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            auto = Camioneta (marca = informacion["Marca"],modelo = informacion["Modelo"],color = informacion["Color"], anio = informacion["Año"], precio = informacion["Precio"])
            auto.save()
            return render(request, 'VehiculosAltaGama/inicio.html')
        
        else:
            miFormulario = CamionetaFormulario()
        
        return render(request, 'VehiculosAltaGama/formulariocamionetas.html',{'miformulario': miFormulario})        
    

def formularioDeportivos(request):
    if request.method == "POST":
        miFormulario = DeportivoFormulario(request.POST) 
        print(miFormulario)
        
        if DeportivoFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            auto = Camioneta (marca = informacion["Marca"],modelo = informacion["Modelo"],color = informacion["Color"], anio = informacion["Año"], precio = informacion["Precio"])
            auto.save()
            return render(request, 'VehiculosAltaGama/inicio.html')
        
        else:
            miFormulario = DeportivoFormulario()
        
        return render(request, 'VehiculosAltaGama/formulariodeportivos.html',{'miformulario': miFormulario})  
    
def formularioSedan(request):
        if request.method == "POST":
            miFormulario = SedanFormulario(request.POST) 
            print(miFormulario)
        
        if SedanFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            auto = Camioneta (marca = informacion["Marca"],modelo = informacion["Modelo"],color = informacion["Color"], anio = informacion["Año"], precio = informacion["Precio"])
            auto.save()
            return render(request, 'VehiculosAltaGama/inicio.html')
        
        else:
            miFormulario = SedanFormulario()
        
        return render(request, 'VehiculosAltaGama/formularioautos.html',{'miformulario': miFormulario})  