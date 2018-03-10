# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

import logging

@api_view()
def general(request, version, microservice, path, format=None):
    return Response({"hola":"mundo"})
