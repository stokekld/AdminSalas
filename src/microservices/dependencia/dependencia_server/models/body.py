# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Body(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, nombre: str=None):
        """
        Body - a model defined in Swagger

        :param nombre: The nombre of this Body.
        :type nombre: str
        """
        self.swagger_types = {
            'nombre': str
        }

        self.attribute_map = {
            'nombre': 'nombre'
        }

        self._nombre = nombre

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.
        :rtype: Body
        """
        return deserialize_model(dikt, cls)

    @property
    def nombre(self) -> str:
        """
        Gets the nombre of this Body.

        :return: The nombre of this Body.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Sets the nombre of this Body.

        :param nombre: The nombre of this Body.
        :type nombre: str
        """

        self._nombre = nombre

