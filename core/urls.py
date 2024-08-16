from django.urls import path
from core import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('blanco/',views.blanco, name = "Blanco"),
    path('about/',views.aboutme, name = "About"),
]





 