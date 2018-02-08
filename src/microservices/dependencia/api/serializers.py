from rest_framework import serializers
# from .models import Dependencia

import logging

class DepSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True, max_length=100)

    def create(self, validated_data):
        logging.info(validated_data)
        return "hola"


