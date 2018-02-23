# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
import random, jwt

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.id = ''.join([random.SystemRandom().choice('abcdef0123456789') for i in range(24)])
        self.client = Client()
        self.token = jwt.encode({
            "perfiles": ["Supervisor", "Solicitante", "Observador", "Analista"],
            "activo": True
        }, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    def test_nopermission(self):
        response = self.client.get('/v1/dependencia/', HTTP_TOKEN=self.token)
        self.assertEqual(response.status_code, 403)
        response = self.client.post('/v1/dependencia/', HTTP_TOKEN=self.token)
        self.assertEqual(response.status_code, 403)

        # El endpoint get /v1/dependencia/id lo puede ocupar cualquiera logeado
        response = self.client.put('/v1/dependencia/' + self.id, HTTP_TOKEN=self.token)
        self.assertEqual(response.status_code, 403)
        response = self.client.delete('/v1/dependencia/' + self.id, HTTP_TOKEN=self.token)
        self.assertEqual(response.status_code, 403)
