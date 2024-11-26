

from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nombre)

class Proyecto(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha = models.DateField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.titulo)

class Consulta(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consulta de {self.nombre} ({self.email})"
    
class Testimonio(models.Model):
    servicio = models.ForeignKey(Servicio, related_name='testimonios', on_delete=models.CASCADE)
    cliente_nombre = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonio de {self.cliente_nombre} para {self.servicio.nombre}"
