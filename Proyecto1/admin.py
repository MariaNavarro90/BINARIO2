from django.contrib import admin
from .models import Servicio, Proyecto, Consulta, Testimonio

admin.site.register(Servicio)
admin.site.register(Proyecto)
admin.site.register(Consulta)
admin.site.register(Testimonio)