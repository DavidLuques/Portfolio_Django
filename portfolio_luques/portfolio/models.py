from django.db import models

# Create your models here.
from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    imagen = models.ImageField(upload_to='proyectos/')

class Habilidad(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    porcentaje = models.IntegerField()
