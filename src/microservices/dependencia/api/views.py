# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
import logging

class ApiView(APIView):
    def get(self, request, format=None):
        logging.info(request.profiles)
        return Response({})
