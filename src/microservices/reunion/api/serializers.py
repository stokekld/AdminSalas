from rest_framework import serializers
from .models import Reunion

import logging

class ResponsableSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True, max_length=150)
    telefono = serializers.CharField(required=True, max_length=50)
    email = serializers.EmailField(required=True)

class ReunionSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    reservo = serializers.CharField(required=True, max_length=24)
    sala = serializers.CharField(required=True, max_length=24)
    dependencia = serializers.CharField(required=True, max_length=24)
    responsable = ResponsableSerializer()
    servicios = serializers.ListField(required=True)
    captura = serializers.DateTimeField(required=True)
    fecha = serializers.DateField(required=True)
    inicio = serializers.TimeField(required=True)
    fin = serializers.TimeField(required=True)
    noPersonas = serializers.IntegerField(required=True)
    description = serializers.CharField()

    def create(self, validated_data):
        reunion = Reunion(**validated_data)
        reunion.save()

        return reunion
