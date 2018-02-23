# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
import random, jwt

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.id = ''
        self.client = Client()
        self.admin = jwt.encode({
            "perfiles": ["Administrador"],
            "activo": True
        }, settings.SECRET_KEY, algorithm='HS256')

    def test_create_dep(self):
        response = self.client.post('/v1/dependencia/', {'nombre':'UCA'}, HTTP_TOKEN=self.admin)
        self.assertEqual(response.status_code, 201)
