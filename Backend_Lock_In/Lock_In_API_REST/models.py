from django.db import models

# Create your models here.

class Objetivo(models.Model):
    nombre= models.CharField(max_length=50)
    tiempo=models.DateTimeField()