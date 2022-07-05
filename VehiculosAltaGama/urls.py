from django.urls import path
from VehiculosAltaGama import views

urlpatterns = [
    path('',views.inicio, name ="Inicio"),
    path('sport',views.sport, name = "Sport"),
    path('sedan',views.sedan, name = "Sedan"),
    path('camioneta', views.camionetas, name = "Camioneta"),
    path('formulario_sedan',views.formulariosedan, name = "FormularioSedan"),
    path('formulario_deportivo', views.formulariodeportivos, name = "FormularioDeportivos"),
    path('formulario_camionetas', views.formulariocamionetas, name = "FormularioCamionetas"),
]
