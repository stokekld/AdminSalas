# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
import random, jwt, logging, requests, json, string

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_deleteUser(self):
        dependencia = {
            "nombre": ''.join(random.choice(string.ascii_lowercase) for _ in range(100)),
            "siglas": ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        }

        response = requests.post('http://dependencia:8080/v1/', data=json.dumps(dependencia), headers={
            'content-type': 'application/json',
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
            "user": ''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
            "password": "123456",
            "activo": True
        }

        response = self.client.post('/v1/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        
        response = self.client.delete('/v1/' + json.loads(response.content)["id"], json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
