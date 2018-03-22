# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import Usuario

import logging, requests, json

def verify_dep(id):
    response = requests.post('http://dependencia:8080/v1/query', data=json.dumps({"query": "{dependencias(filter: {id:\"" + id + "\"}){id}}"}), headers={'content-type': 'application/json'})

    deps = json.loads(response.text)

    if len(deps['data']['dependencias']) is not 1:
        return False

    return True

class MainView(APIView):

    def post(self, request, format=None):

        many = True if isinstance(request.data, list) else False

        serializer = UserSerializer(data=request.data, many=many)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        if not verify_dep(serializer.validated_data['dependencia']):
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

        if not verify_dep(serializer.validated_data['dependencia']):
            return Response({'dependencia': ["Debe ser una dependencia válida."]}, 400)

        serializer.save()

        return Response(serializer.data, 200)

    def delete(self, request, id, format=None):

        if Usuario.objects(id=id).count() is not 1:
            return HttpResponse(status=404)

        usuario = Usuario.objects(id=id)[0]
        usuario.delete()

        return HttpResponse(status=200)
