from rest_framework import serializers
from .models import Objetivo, Post

class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Objetivo
        fields='__all__' #foreignkey

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields='__all__'