# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SalaSerializer
from .models import Sala

class MainView(APIView):

    def post(self, request, format=None):

        many = True if isinstance(request.data, list) else False

        serializer = SalaSerializer(data=request.data, many=many)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        serializer.save()

        return Response(serializer.data, 201)
