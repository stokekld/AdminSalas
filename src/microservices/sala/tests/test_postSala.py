# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
import random, logging, requests, json, string

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_postUser(self):
        sala = {
            "nombre": ''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
            "capNormal": 100,
            "capMax": 100
        }

        response = self.client.post('/v1/', json.dumps(sala), content_type='application/json')
        self.assertEqual(response.status_code, 201)
