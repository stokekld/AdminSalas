# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
import random, jwt, logging, requests, json, string, datetime

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.client = Client()
        self.headers = {
            'content-type': 'application/json'
        }

    def test_postUser(self):
            # POST DEPENDENCIA
        dependencia = {
            "nombre": ''.join(random.choice(string.ascii_lowercase) for _ in range(100)),
            "siglas": ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        }

        response = requests.post('http://dependencia:8080/v1/', data=json.dumps(dependencia), headers=self.headers)
        self.assertEqual(response.status_code, 201)

        idDependencia = json.loads(response.content)["id"]

        # POST USUARIO
        usuario = {
            "datos": {
                "nombre": "Ricardo",
                "apaterno": "Guerra",
                "amaterno": "Suarez",
                "email": "ejemplo@ejemplo.com",
                "telefono": "Ext: 12345"
                },
            "dependencia": idDependencia,
            "perfiles": ["Supervisor", "Solicitante", "Observador", "Analista"],
            "user": ''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
            "password": "123456",
            "activo": True
        }

        response = requests.post('http://usuario:8080/v1/', data=json.dumps(usuario), headers=self.headers)
        self.assertEqual(response.status_code, 201)

        idUsuario = json.loads(response.content)["id"]

        # POST SALA
        sala = {
            "nombre": ''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
            "capNormal": 100,
            "capMax": 100
        }

        response = requests.post('http://sala:8080/v1/', data=json.dumps(sala), headers=self.headers)
        self.assertEqual(response.status_code, 201)

        idSala = json.loads(response.content)["id"]

        # POST REUNION
        reuniones = {
            "reservo": idUsuario,
            "sala": idSala,
            "dependencia": idDependencia,
            "responsable": {
                "nombre": "Ricardo Guerra Suarez",
                "telefono": "Ext: 12345",
                "email": "ejemplo@ejemplo.com"
            },
            "servicios": [
                "Cafeteria"
            ],
            "captura": datetime.datetime.now().strftime("%Y-%m-%d"),
            "fecha": datetime.datetime.now().strftime("%Y-%m-%d"),
            "inicio": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "fin": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "noPersonas": 0,
            "description": "string"
        }

        response = self.client.post("/v1/", json.dumps(reuniones), content_type='application/json')
        self.assertEqual(response.status_code, 201)
