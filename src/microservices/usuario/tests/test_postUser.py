# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
import random, jwt, logging

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.client = Client()
        self.admin = jwt.encode({
            "perfiles": ["Administrador"],
            "activo": True
        }, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    def test_postUser(self):

        response = self.client.post('/v1/dependencia/', {"nombre":"Dependencia"}, content_type='application/json', HTTP_TOKEN=self.admin)
        self.assertEqual(response.status_code, 201)

        id = response.data['id']

        response = self.client.post('/v1/usuario', {
            "datos": {
                "nombre": "Ricardo",
                "apaterno": "Guerra",
                "amaterno": "Suarez",
                "email": "ejemplo@ejemplo.com",
                "telefono": "Ext: 12345"
            },
            "dependencia": id,
            "perfiles": ["Supervisor", "Solicitante", "Observador", "Analista"],
            "password": "123456",
            "activo": True
        }, content_type='application/json', HTTP_TOKEN=self.admin)
        self.assertEqual(response.status_code, 201)

        response = self.client.delete('/v1/dependencia/' + id, HTTP_TOKEN=self.admin)
        self.assertEqual(response.status_code, 200)



