# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import *

class Datos(EmbeddedDocument):
    nombre = StringField(max_length=50, required=True)
    apaterno = StringField(max_length=50, required=True)
    amaterno = StringField(max_length=50, required=True)
    email = EmailField(required=True)
    telefono = StringField(max_length=50, required=True)

class Usuario(Document):
    datos = EmbeddedDocumentField(Datos)
    dependencia = ObjectIdField(required=True)
    perfiles = ListField(required=True)
    user= StringField(max_length=10, required=True, unique=True)
    password = StringField(max_length=64, required=True)
    activo = BooleanField(required=True)
