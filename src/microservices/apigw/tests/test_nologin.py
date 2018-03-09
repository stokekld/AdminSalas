# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
from datetime import datetime, timedelta
import jwt, logging

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.tokens = [
            {
                "exp": datetime.utcnow() - timedelta(seconds=60),
                "id": "1234455678890",
                "perfiles": [],
                "activo": True
            },
            {
                "exp": datetime.utcnow() + timedelta(seconds=60),
                "perfiles": [],
                "activo": True
            },
            {
                "exp": datetime.utcnow() + timedelta(seconds=60),
                "id": "1234455678890",
                "activo": True
            },
            {
                "exp": datetime.utcnow() + timedelta(seconds=60),
                "id": "1234455678890",
                "perfiles": []
            },
            {
                "exp": datetime.utcnow() + timedelta(seconds=60),
                "id": "1234455678890",
                "perfiles": [],
                "activo": False
            }
        ]
        self.client = Client()

    def test_nologin(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 401)

        for token in self.tokens:
            hash = jwt.encode(token, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
            response = self.client.get('/', HTTP_TOKEN=hash)
            self.assertEqual(response.status_code, 401)
