from django.urls import path
from VehiculosAltaGama import views

urlpatterns = [
    path('',views.inicio, name ="Inicio"),
    path('sport',views.sport, name = "Sport"),
    path('sedan',views.sedan, name = "Sedan"),
    path('camioneta', views.camionetas, name = "Camioneta"),
    path('formulario_sedan',views.formularioSedan, name = "FormularioSedan"),
    path('formulario_deportivo', views.formularioDeportivos, name = "FormularioDeportivos"),
    path('formulario_camionetas', views.formularioCamionetas, name = "FormularioCamionetas"),
]
