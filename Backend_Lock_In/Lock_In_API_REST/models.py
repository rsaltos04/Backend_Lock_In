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

