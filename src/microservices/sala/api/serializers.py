from rest_framework import serializers
from .models import Sala

class SalaSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    nombre = serializers.CharField(required=True, max_length=10)
    capNormal = serializers.IntegerField(required=True)
    capMax = serializers.IntegerField(required=True)

    def create(self, validated_data):

        sala = Sala(**validated_data)
        sala.save()

        return sala

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.capNormal = validated_data.get('capNormal', instance.capNormal)
        instance.capMax = validated_data.get('capMax', instance.capMax)

        return instance
