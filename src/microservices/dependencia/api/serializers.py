from rest_framework import serializers
from .models import Dependencia

import logging

class DepSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    nombre = serializers.CharField(max_length=100, required=True)

    def create(self, validated_data):

        dependencia = Dependencia(**validated_data)
        dependencia.save()

        return dependencia

    def update(self, instance, validated_data):

        instance.nombre = validated_data['nombre']
        instance.save()

        return instance
