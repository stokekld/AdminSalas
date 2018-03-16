# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import QueryDict
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests, logging, json

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def general(request, version, microservice, path, format=None):

    port = 8080

    url = ('http://%s:%s/%s/%s') % (microservice, port, version, path)

    response = requests.request(request.method.lower(), url, params=QueryDict(request.META['QUERY_STRING']).dict(), data=request.body, headers={'content-type': request.content_type})

    if response.headers['Content-Type'] == 'application/json':
        return Response(json.loads(response.text), response.status_code, headers=response.headers)
    else:
        return Response(response.text, response.status_code, headers=response.headers)

