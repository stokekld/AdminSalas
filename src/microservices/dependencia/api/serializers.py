from rest_framework import serializers
from .models import Dependencia

import logging

class DepSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    nombre = serializers.CharField(max_length=100, required=True)

    def create(self, validated_data):

        dependencia = Dependencia()
        dependencia.nombre = validated_data['nombre']
        dependencia.save()

        serializers = DepSerializer(dependencia)

        return serializers.data

    def update(self, instance, validated_data):

        instance.nombre = validated_data['nombre']
        instance.save()

        serializers = DepSerializer(instance)

        return serializers.data
