from django.urls import path
from . import views
from .views import github_proyectos
from django.contrib import admin



urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.servicios, name='servicios'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicio/<int:id>/', views.detalle_servicio, name='detalle_servicio'),
    path('proyecto/<int:id>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('buscar/', views.buscar, name='buscar'),
    path("api/github/proyectos", github_proyectos, name="github_proyectos"),
    path('admin/', admin.site.urls), 
    
]