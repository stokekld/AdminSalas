from rest_framework import permissions
from django.urls import resolve
import logging

class ProfilePermission(permissions.BasePermission):
    
    message = 'Recurso no permitido.'
    admin = 'Administrador'

    def has_permission(self, request, view):

        return True
