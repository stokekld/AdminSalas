# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer

import logging, requests

class MainView(APIView):

    def post(self, request, format=None):

        many = True if isinstance(request.data, list) else False

        serializer = UserSerializer(data=request.data, many=many)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        ## Verificando dependencia
        response = requests.get('http://apigw/v1/dependencia/' + serializer.validated_data['dependencia'], headers={
            'token': request.META['HTTP_TOKEN']
        })

        if not response.status_code == 200:
            return Response({'dependencia': ["Debe ser una dependencia válida."]}, 400)

        serializer.save()

        return Response(serializer.data, 201)
