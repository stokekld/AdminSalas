# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
import random, jwt, logging, requests, json

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.client = Client()
        self.admin = jwt.encode({
            "perfiles": ["Administrador"],
            "activo": True
        }, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    def test_postUser(self):

        response = requests.post('http://apigw/v1/dependencia/', data=json.dumps({"nombre":"Dependencia"}), headers={
            'content-type': 'application/json',
            'token': self.admin
        })
        self.assertEqual(response.status_code, 201)

        id = json.loads(response.content)["id"]

        data = {
            "datos": {
                "nombre": "Ricardo",
                "apaterno": "Guerra",
                "amaterno": "Suarez",
                "email": "ejemplo@ejemplo.com",
                "telefono": "Ext: 12345"
            },
            "dependencia": id,
            "perfiles": ["Supervisor", "Solicitante", "Observador", "Analista"],
            "user": "rootroot",
            "password": "123456",
            "activo": True
        }

        response = self.client.post('/v1/usuario/', json.dumps(data), content_type='application/json', HTTP_TOKEN=self.admin)
        self.assertEqual(response.status_code, 201)

        response = requests.delete('http://apigw/v1/dependencia/' + id, headers={
            'content-type': 'application/json',
            'token': self.admin
        })
        self.assertEqual(response.status_code, 200)



