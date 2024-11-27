from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("servicios/", views.servicios, name="servicios"),
    path("proyectos/", views.proyectos, name="proyectos"),
    path("contacto/", views.contacto, name="contacto"),
    path("servicio/<int:id>/", views.detalle_servicio, name="detalle_servicio"),
    path("proyecto/<int:id>/", views.detalle_proyecto, name="detalle_proyecto"),
    path("buscar/", views.buscar, name="buscar"),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
