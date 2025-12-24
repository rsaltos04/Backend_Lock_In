from rest_framework import serializers
from .models import Objetivo, Post, Corazones, SesionEnfoque

class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Objetivo
        fields='__all__' #foreignkey

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields='__all__'

class SesionEnfoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model= SesionEnfoque
        fields='__all__'

    def validate(self, data):
        if data['minutos_totales'] < data['minutos_segundo_plano']:
            raise serializers.ValidationError(
                "Los minutos totales deben ser mayores o iguales a los minutos en segundo plano.")
        return data

class CorazonesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Corazones
        fields='__all__'