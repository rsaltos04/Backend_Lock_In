from rest_framework import serializers
from .models import Objetivo

class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Objetivo
        fields='__all__' #foreignkey
    