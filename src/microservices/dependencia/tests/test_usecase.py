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
        self.user= jwt.encode({
            "perfiles": ["Supervisor", "Solicitante", "Observador", "Analista"],
            "activo": True
        }, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    def test_crudDep(self):
        response = self.client.post("/v1/dependencia/", '{"nombre":"nombre1"}', content_type='application/json', HTTP_TOKEN=self.admin)
        self.assertEqual(response.status_code, 201)

        id = response.data['id']

        response = self.client.get('/v1/dependencia/' + id, HTTP_TOKEN=self.user)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/v1/dependencia/' + id, HTTP_TOKEN=self.admin)
        self.assertEqual(response.status_code, 200)

        response = self.client.put('/v1/dependencia/' + id, HTTP_TOKEN=self.user)
        self.assertEqual(response.status_code, 403)
        response = self.client.put('/v1/dependencia/' + id, '{"nombre":"nombre2"}', content_type='application/json', HTTP_TOKEN=self.admin)
        self.assertEqual(response.status_code, 200)

        response = self.client.delete('/v1/dependencia/' + id, HTTP_TOKEN=self.user)
        self.assertEqual(response.status_code, 403)
        response = self.client.delete('/v1/dependencia/' + id, HTTP_TOKEN=self.admin)
        self.assertEqual(response.status_code, 200)


    def test_getAll(self):
        response = self.client.get('/v1/dependencia/', HTTP_TOKEN=self.admin)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/v1/dependencia/', HTTP_TOKEN=self.user)
        self.assertEqual(response.status_code, 403)
