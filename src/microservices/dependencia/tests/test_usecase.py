# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
import random, jwt, logging, json

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_crudDep(self):
        dependencia = {
            "nombre": "nombre1",
            "siglas": "siglas1"
        }

        response = self.client.post("/v1/", json.dumps(dependencia), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        id = response.data['id']

        response = self.client.get('/v1/' + id)
        self.assertEqual(response.status_code, 200)

        dependencia = {
            "nombre": "nombre2",
            "siglas": "siglas2"
        }

        response = self.client.put('/v1/' + id, json.dumps(dependencia), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.delete('/v1/' + id)
        self.assertEqual(response.status_code, 200)


    def test_getAll(self):
        response = self.client.get('/v1/')
        self.assertEqual(response.status_code, 200)
