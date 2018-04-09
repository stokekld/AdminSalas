from django.http import HttpResponse
from django.conf import settings
import os, jwt, logging


class AuthMiddleware(object):

    novalidation = [
        '/v1/usuario/auth'
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def getDataToken(self, token):
        """
        Obteniendo token de headers
        """
        return jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)

    def validToken(self, request):
        """
        Valida token
        """
        # Verifica cabecera token
        if not 'HTTP_TOKEN' in request.META:
            return False

        # decodificando token
        try:
            data = self.getDataToken(request.META['HTTP_TOKEN'])
        except Exception as e:
            return False

        # Obteniendo id
        if not 'id' in data:
            return False

        # Obteniendo perfiles
        if not 'perfiles' in data:
            return False

        # Verificando si es activo
        if not 'activo' in data or not data['activo']:
            return False

        return True

    def __call__(self, request):

        if not request.path in self.novalidation:
            if not self.validToken(request):
                return HttpResponse(status=401)

        response = self.get_response(request)

        return response
