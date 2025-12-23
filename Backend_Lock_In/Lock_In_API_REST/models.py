from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Objetivo(models.Model):
    nombre= models.CharField(max_length=50)
    caducidad=models.DateTimeField()
    id_autor=models.ForeignKey(User,
                               on_delete=models.CASCADE)
    descripcion= models.CharField(max_length=150, blank=True)
    categoria=models.CharField(max_length=50)
    completado=models.BooleanField(default=False)

class Post(models.Model):

    class Etiqueta(models.TextChoices):
        LOGRO = "Logros"
        AYUDA = "Ayuda"
        MOTIVACION = "Motivación"


    id_autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    corazones = models.IntegerField(default=0)
    mensaje = models.TextField(max_length=200)
    etiqueta = models.CharField(max_length=10, choices=Etiqueta.choices)


