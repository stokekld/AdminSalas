# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import *

class Sala(Document):
    nombre = StringField(max_length=10, required=True)
    capNormal = IntField(required=True)
    capMax = IntField(required=True)

