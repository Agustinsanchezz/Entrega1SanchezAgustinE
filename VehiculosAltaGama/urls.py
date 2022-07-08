from django.urls import path
from VehiculosAltaGama import views

urlpatterns = [
    path('',views.inicio, name ="Inicio"),
    path('sport',views.sport, name = "Sport"),
    path('sedan',views.sedan, name = "Sedan"),
    path('camioneta', views.camionetas, name = "Camioneta"),
    path('formulario_sedan',views.formulario_sedan, name = "FormularioSedan"),
    path('formulario_deportivo', views.formulario_deportivos, name = "FormularioDeportivos"),
    path('formulario_camionetas', views.formulario_camionetas, name = "FormularioCamionetas"),
]
