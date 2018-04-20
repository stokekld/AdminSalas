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
    captura = serializers.DateField(required=True)
    fecha = serializers.DateField(required=True)
    inicio = serializers.DateTimeField(required=True)
    fin = serializers.DateTimeField(required=True)
    noPersonas = serializers.IntegerField(required=True)
    description = serializers.CharField()

    def create(self, validated_data):
        reunion = Reunion(**validated_data)
        reunion.save()

        return reunion

    def update(self, instance, validated_data):
        instance.reservo = validated_data.get('reservo', instance.reservo)
        instance.sala = validated_data.get('sala', instance.sala)
        instance.dependencia = validated_data.get('dependencia', instance.dependencia)
        instance.responsable.nombre = validated_data['responsable'].get('nombre', instance.responsable.nombre)
        instance.responsable.telefono = validated_data['responsable'].get('telefono', instance.responsable.telefono)
        instance.responsable.email = validated_data['responsable'].get('email', instance.responsable.email)
        instance.servicios = validated_data.get('servicios', instance.servicios)
        instance.captura = validated_data.get('captura', instance.captura)
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.inicio = validated_data.get('inicio', instance.inicio)
        instance.fin = validated_data.get('fin', instance.fin)
        instance.noPersonas = validated_data.get('noPersonas', instance.noPersonas)
        instance.description = validated_data.get('description', instance.description)
        return instance
