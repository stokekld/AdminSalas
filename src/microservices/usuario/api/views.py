# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response

class MainView(APIView):

    def post(self, request, format=None):
        return Response()
