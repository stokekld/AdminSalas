# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from permissions.profiles import ProfilePermission

from .serializers import DepSerializer

import logging

class ApiView(APIView):

    permission_classes = (ProfilePermission,)

    def get(self, request, format=None):
        return Response({})

    def post(self, request, format=None):

        many = True if isinstance(request.data, list) else False

        serializer = DepSerializer(data=request.data, many=many)

        if not serializer.is_valid():
            return HttpResponse(status=400)

        dependencia = serializer.save()

        logging.info(dependencia)

        return Response({})
