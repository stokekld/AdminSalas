# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import DepSerializer
from .models import Dependencia
from .schema import schema

import logging

class QueryView(APIView):

    def post(self, request, format=None):

        try:
            result = schema.execute(request.data['query'])
        except:
            return Response({}, 400)

        if result.data is None:
            return Response({}, 400)

        return Response(result.data['dependencia'])

class MainView(APIView):

    def post(self, request, format=None):

        many = True if isinstance(request.data, list) else False

        serializer = DepSerializer(data=request.data, many=many)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        serializer.save()

        return Response(serializer.data, 201)

class IdView(APIView):

    def get(self, request, id, format=None):

        if Dependencia.objects(id=id).count() is not 1:
            return HttpResponse(status=404)

        dependencia = Dependencia.objects(id=id)[0]
        serializer = DepSerializer(dependencia)
        return Response(serializer.data)

    def put(self, request, id, format=None):

        if Dependencia.objects(id=id).count() is not 1:
            return HttpResponse(status=404)

        dependencia = Dependencia.objects(id=id)[0]

        serializer = DepSerializer(dependencia, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        serializer.save()

        return Response(serializer.data)

    def delete(self, request, id, format=None):

        if Dependencia.objects(id=id).count() is not 1:
            return HttpResponse(status=404)

        dependencia = Dependencia.objects(id=id)[0]
        dependencia.delete()

        return HttpResponse(status=200)
