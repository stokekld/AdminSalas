# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
import jwt

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.token = jwt.encode({
                "perfiles": ["Administrador", "Supervisor", "Solicitante", "Observador", "Analista"],
                "activo": False
            }, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        self.client = Client()

    def test_nologin(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 401)
