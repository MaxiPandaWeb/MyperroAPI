from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quienes', views.quienes, name='quienes'),
    path('contacto', views.contacto, name='contacto'),
    path('nuevo', views.nuevo, name='nuevo'),
    path('mostrar', views.mostrar, name='mostrar'),
    path('mostrarcontacto', views.mostrarcontacto, name='mostrarcontacto'),
]
