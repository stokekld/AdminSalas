# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
import random, jwt

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.id = ''.join([random.SystemRandom().choice('abcdef0123456789') for i in range(24)])
        self.token = jwt.encode({
                "perfiles": ["Administrador", "Supervisor", "Solicitante", "Observador", "Analista"],
                "activo": False
            }, settings.SECRET_KEY, algorithm='HS256')
        self.client = Client()

    def test_nologin(self):
        response = self.client.get('/v1/dependencia/')
        self.assertEqual(response.status_code, 401)
        response = self.client.post('/v1/dependencia/')
        self.assertEqual(response.status_code, 401)

        response = self.client.get('/v1/dependencia/' + self.id)
        self.assertEqual(response.status_code, 401)
        response = self.client.post('/v1/dependencia/' + self.id)
        self.assertEqual(response.status_code, 401)
        response = self.client.put('/v1/dependencia/' + self.id)
        self.assertEqual(response.status_code, 401)
        response = self.client.delete('/v1/dependencia/' + self.id)
        self.assertEqual(response.status_code, 401)


        response = self.client.get('/v1/dependencia/', HTTP_TOKEN=self.token)
        self.assertEqual(response.status_code, 401)
        response = self.client.post('/v1/dependencia/', HTTP_TOKEN=self.token)
        self.assertEqual(response.status_code, 401)

        response = self.client.get('/v1/dependencia/' + self.id, HTTP_TOKEN=self.token)
        self.assertEqual(response.status_code, 401)
        response = self.client.post('/v1/dependencia/' + self.id, HTTP_TOKEN=self.token)
        self.assertEqual(response.status_code, 401)
        response = self.client.put('/v1/dependencia/' + self.id, HTTP_TOKEN=self.token)
        self.assertEqual(response.status_code, 401)
        response = self.client.delete('/v1/dependencia/' + self.id, HTTP_TOKEN=self.token)
        self.assertEqual(response.status_code, 401)
