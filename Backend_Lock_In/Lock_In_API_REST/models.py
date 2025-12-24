from django.db import models
from django.contrib.auth.models import User
from django.db.models import CheckConstraint, Q, F


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
    mensaje = models.TextField(max_length=200)
    etiqueta = models.CharField(max_length=10, choices=Etiqueta.choices)

class SesionEnfoque(models.Model):
    id_objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)
    minutos_totales = models.IntegerField()
    minutos_segundo_plano = models.IntegerField()

    class Meta:
        constraints = [
            CheckConstraint(
                condition=Q(minutos_totales__gte=F('minutos_segundo_plano')),
                name="totales_gte_segundo_plano"
            )
        ]

class Corazones(models.Model):
    id_post =  models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    id_autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    corazon = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id_autor', 'id_post'],
                name='unique_autor_post_relacion'
            )
        ]