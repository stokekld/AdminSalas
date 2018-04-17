# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import *

class Responsable(EmbeddedDocument):
    nombre = StringField(max_length=150, required=True)
    telefono = StringField(max_length=50, required=True)
    email = EmailField(required=True)

class Reunion(Document):
    reservo = ObjectIdField(required=True)
    sala = ObjectIdField(required=True)
    dependencia = ObjectIdField(required=True)
    responsable = EmbeddedDocumentField(Responsable)
    servicios = ListField(required=True)
    captura = DateTimeField(required=True)
    fecha = DateTimeField(required=True)
    inicio = DateTimeField(required=True)
    fin = DateTimeField(required=True)
    noPersonas = IntField(required=True)
    description = StringField()
