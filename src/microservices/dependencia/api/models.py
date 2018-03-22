# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import *

class Dependencia(Document):
    nombre = StringField(max_length=100, required=True)
    siglas = StringField(max_length=10, required=True, unique=True)
