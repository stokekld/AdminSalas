# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import *

class Dependencia(Document):
    nombre = StringField(max_length=100, required=True)
