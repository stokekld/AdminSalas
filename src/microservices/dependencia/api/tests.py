# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_nologin(self):
        response = self.client.get('/v1/dependencia/')
        self.assertEqual(response.status_code, 401)
        response = self.client.post('/v1/dependencia/')
        self.assertEqual(response.status_code, 401)
