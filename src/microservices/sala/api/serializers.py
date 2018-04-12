from rest_framework import serializers
from .models import Sala

class SalaSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True, max_length=10)
    capNormal = serializers.IntegerField(required=True)
    capMax = serializers.IntegerField(required=True)

    def create(self, validated_data):

        sala = Sala(**validated_data)
        sala.save()

        return sala
