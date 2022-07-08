from django.shortcuts import render
from django.http import HttpResponse
import VehiculosAltaGama
from VehiculosAltaGama.models import Sedan, Camioneta, Deportivo
from VehiculosAltaGama.forms import SedanFormulario, CamionetaFormulario, DeportivoFormulario

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
    return render(request, 'VehiculosAltaGama/Inicio.html')



def formulario_camionetas(request):
    if request.method == "POST":
            miFormulario = CamionetaFormulario(request.POST) 
            print(miFormulario)
        
            if CamionetaFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                auto = Camioneta (marca = informacion["Marca"],modelo = informacion["Modelo"],color = informacion["Color"], anio = informacion["Año"], precio = informacion["Precio"])
                auto.save()
                return render(request, 'VehiculosAltaGama/Inicio.html')
        
    else:
            miFormulario = CamionetaFormulario()
        
    return render(request, 'VehiculosAltaGama/formulario_camionetas.html',{'miformulario': miFormulario})        
    

def formulario_deportivos(request):
    if request.method == "POST":
            miFormulario = DeportivoFormulario(request.POST) 
            print(miFormulario)
        
            if DeportivoFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                auto = Deportivo (marca = informacion["Marca"],modelo = informacion["Modelo"],color = informacion["Color"], anio = informacion["Año"], precio = informacion["Precio"])
                auto.save()
                return render(request, 'VehiculosAltaGama/Inicio.html')
        
    else:
            miFormulario = DeportivoFormulario()
        
    return render(request, 'VehiculosAltaGama/formulario_deportivos.html',{'miformulario': miFormulario})  
    
def formulario_sedan(request):
    if request.method == "POST":
        
            miFormulario = SedanFormulario(request.POST) 
            
            print(miFormulario)
        
            if SedanFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                
                auto = Sedan (marca = informacion["Marca"],modelo = informacion["Modelo"],color = informacion["Color"], anio = informacion["Año"], precio = informacion["Precio"])
                
                auto.save()
                
                return render(request, 'VehiculosAltaGama/Inicio.html')
        
    else:
            miFormulario = SedanFormulario()
        
    return render(request, 'VehiculosAltaGama/formulario_sedan.html',{'miformulario': miFormulario})  



def buscarCamioneta(request):
    if request.GET.get("marca"):
        #print(str(request.GET("marca").values()))
        MODELO = request.GET.get("marca")
        busqueda = Camioneta.objects.filter(modelo__icontains=MODELO)
        return render(request, "VehiculosAltaGama/busqueda.html", {'Camionetahtml':busqueda})
    else:
        #print("ELSE")
        busqueda = Camioneta.objects.all()
        
        return render(request,"VehiculosAltaGama/busqueda.html", {'Camionetahtml':busqueda})
    