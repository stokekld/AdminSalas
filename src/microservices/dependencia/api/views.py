# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from permissions.profiles import ProfilePermission

from .serializers import DepSerializer
from .models import Dependencia

import logging

class MainView(APIView):

    permission_classes = (ProfilePermission,)

    def get(self, request, format=None):
        dependencias = Dependencia.objects.all()
        serializer = DepSerializer(dependencias, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        many = True if isinstance(request.data, list) else False

        serializer = DepSerializer(data=request.data, many=many)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        dependencia = serializer.save()

        return Response(dependencia)

class IdView(APIView):

    permission_classes = (ProfilePermission,)

    def get(self, request, id, format=None):
        dependencia = Dependencia.objects(id=id)
        serializer = DepSerializer(dependencia, many=True)
        return Response(serializer.data)
