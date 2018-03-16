# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase, Client
from django.conf import settings
import random, jwt, logging

class TestMicroservice(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_crudDep(self):
        response = self.client.post("/v1/", '{"nombre":"nombre1"}', content_type='application/json')
        self.assertEqual(response.status_code, 201)

        id = response.data['id']

        response = self.client.get('/v1/' + id)
        self.assertEqual(response.status_code, 200)

        response = self.client.put('/v1/' + id, '{"nombre":"nombre2"}', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.delete('/v1/' + id)
        self.assertEqual(response.status_code, 200)


    def test_getAll(self):
        response = self.client.get('/v1/')
        self.assertEqual(response.status_code, 200)
