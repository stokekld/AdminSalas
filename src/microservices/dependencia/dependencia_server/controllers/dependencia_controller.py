import connexion
from dependencia_server.models.body import Body
from dependencia_server.models.dependencia import Dependencia
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_one(body):
    """
    Agrega una dependencia
    Agrega una dependencia si el perfil de usuario es Administrador
    :param body: 
    :type body: dict | bytes

    :rtype: Dependencia
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())
    return 'do some magic!'


def delete_by_id(id):
    """
    Elimina una dependencia
    Elimina una depenpendencia si el usuario es Administrador y no se ha usado para una reunión
    :param id: Id de la dependencia
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all():
    """
    Lista de dependencias
    Genera la lista completa de dependencias

    :rtype: List[Dependencia]
    """
    return 'do some magic!'


def get_by_id(id):
    """
    Regresa una dependencia
    
    :param id: Id de la dependencia
    :type id: int

    :rtype: Dependencia
    """
    return 'do some magic!'


def update_by_id(id):
    """
    Actualiza una dependencia
    Actualiza una dependencia si el usuario es Administrador
    :param id: Id de la dependencia
    :type id: int

    :rtype: Dependencia
    """
    return 'do some magic!'
