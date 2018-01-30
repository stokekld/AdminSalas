# coding: utf-8

from __future__ import absolute_import

from dependencia_server.models.body import Body
from dependencia_server.models.dependencia import Dependencia
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDependenciaController(BaseTestCase):
    """ DependenciaController integration test stubs """

    def test_add_one(self):
        """
        Test case for add_one

        Agrega una dependencia
        """
        body = Body()
        response = self.client.open('/v1/dependencia//',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_by_id(self):
        """
        Test case for delete_by_id

        Elimina una dependencia
        """
        response = self.client.open('/v1/dependencia//{id}'.format(id=789),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_all(self):
        """
        Test case for get_all

        Lista de dependencias
        """
        response = self.client.open('/v1/dependencia//',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_by_id(self):
        """
        Test case for get_by_id

        Regresa una dependencia
        """
        response = self.client.open('/v1/dependencia//{id}'.format(id=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_by_id(self):
        """
        Test case for update_by_id

        Actualiza una dependencia
        """
        response = self.client.open('/v1/dependencia//{id}'.format(id=789),
                                    method='PUT',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
