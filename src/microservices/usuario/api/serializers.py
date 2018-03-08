from rest_framework import serializers
from .models import Usuario

import logging, hashlib

class Dataserializer(serializers.Serializer):
    nombre = serializers.CharField(required=True, max_length=50)
    apaterno = serializers.CharField(required=True, max_length=50)
    amaterno = serializers.CharField(required=True, max_length=50)
    email = serializers.EmailField(required=True)
    telefono = serializers.CharField(required=True, max_length=50)

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    datos = Dataserializer()
    dependencia = serializers.CharField(required=True, max_length=24)
    perfiles = serializers.ListField(required=True)
    user = serializers.CharField(required=True, max_length=10)
    password = serializers.CharField(required=True, max_length=64)
    activo = serializers.BooleanField(required=True)

    def create(self, validated_data):

        usuario = Usuario(**validated_data)
        usuario.password = hashlib.sha256(usuario.password.encode("UTF-8")).hexdigest()
        usuario.save()

        return usuario

