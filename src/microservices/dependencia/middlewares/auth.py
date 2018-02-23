from django.http import HttpResponse
from django.conf import settings
import os, jwt, logging


class Auth(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def getDataToken(self, token):
        """
        Obteniendo token de headers
        """
        return jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)

    def __call__(self, request):

        # Verifica cabecera token
        if not 'HTTP_TOKEN' in request.META:
            return HttpResponse(status=401)

        # decodificando token
        try:
            data = self.getDataToken(request.META['HTTP_TOKEN'])
        except Exception as e:
            logging.warning(str(e))
            return HttpResponse(status=401)

        # Verificando si es activo
        if not 'activo' in data or not data['activo']:
            return HttpResponse(status=401)

        # Obteniendo perfiles
        if not 'perfiles' in data:
            return HttpResponse(status=401)

        request.profiles = data['perfiles']

        response = self.get_response(request)

        return response
