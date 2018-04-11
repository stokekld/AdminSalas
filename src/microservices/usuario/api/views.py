# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from .serializers import UserSerializer
from .models import Usuario

import logging, requests, json, hashlib, datetime, jwt

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

class AuthView(APIView):

    seconds = 300

    def post(self, request, format=None):

        if not 'user' in request.data and not 'password' in request.data:
            return Response(serializer.errors, 400)

        user = request.data['user']
        password = request.data['password']

        usuario = Usuario.objects(user=user, password=hashlib.sha256(password.encode("UTF-8")).hexdigest())

        if usuario.count() is not 1:
            return HttpResponse(status=404)

        tokenInfo = {
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=self.seconds),
            "id": str(usuario[0].id),
            "datos": {
                "nombre": usuario[0].datos.nombre,
                "apaterno": usuario[0].datos.apaterno,
                "amaterno": usuario[0].datos.amaterno,
                "email": usuario[0].datos.email,
                "telefono": usuario[0].datos.telefono
            },
            "perfiles": usuario[0].perfiles,
            "user": usuario[0].user,
            "activo": usuario[0].activo
        }

        try:
            token = jwt.encode(tokenInfo, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        except Exception as e:
            return HttpResponse(status=400)

        return Response({'token': token}, 201)

    def put(self, request, format=None):
        if not 'token' in request.data:
            return Response(serializer.errors, 400)

        try:
            data = jwt.decode(request.data['token'], settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        except Exception as e:
            return HttpResponse(status=400)

        data['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.seconds)

        try:
            token = jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        except Exception as e:
            return HttpResponse(status=400)

        return Response({'token': token}, 200)
