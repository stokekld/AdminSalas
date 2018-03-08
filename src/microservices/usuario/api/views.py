# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import Usuario

import logging, requests

def verify_dep(id, token):
    response = requests.get('http://apigw/v1/dependencia/' + id, headers={
        'token': token
    })

    return response.status_code

class MainView(APIView):

    def post(self, request, format=None):

        many = True if isinstance(request.data, list) else False

        serializer = UserSerializer(data=request.data, many=many)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        if not verify_dep(serializer.validated_data['dependencia'], request.META['HTTP_TOKEN']) == 200:
            return Response({'dependencia': ["Debe ser una dependencia válida."]}, 400)

        serializer.save()

        return Response(serializer.data, 201)

class IdView(APIView):

    def put(self, request, id, format=None):

        if Usuario.objects(id=id).count() is not 1:
            return HttpResponse(status=404)

        usuario = Usuario.objects(id=id)[0]

        serializer = UserSerializer(usuario, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        if not verify_dep(serializer.validated_data['dependencia'], request.META['HTTP_TOKEN']) == 200:
            return Response({'dependencia': ["Debe ser una dependencia válida."]}, 400)

        serializer.save()

        return Response(serializer.data, 200)
