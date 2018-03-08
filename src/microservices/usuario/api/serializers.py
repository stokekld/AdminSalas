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

    def update(self, instance, validated_data):

        instance.datos.nombre = validated_data['datos'].get('nombre', instance.datos.nombre)
        instance.datos.apaterno = validated_data['datos'].get('apaterno', instance.datos.apaterno)
        instance.datos.amaterno = validated_data['datos'].get('amaterno', instance.datos.amaterno)
        instance.datos.email = validated_data['datos'].get('email', instance.datos.email)
        instance.datos.telefono = validated_data['datos'].get('telefono', instance.datos.telefono)
        instance.dependencia = validated_data.get('dependencia', instance.dependencia)
        instance.perfiles = validated_data.get('perfiles', instance.perfiles)
        instance.user = validated_data.get('user', instance.user)
        instance.password = hashlib.sha256(validated_data['password'].encode("UTF-8")).hexdigest() if 'password' in validated_data else instance.password
        instance.activo = validated_data.get('activo', instance.activo)

        return instance
