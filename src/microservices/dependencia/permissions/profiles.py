from rest_framework import permissions
from django.urls import resolve
import logging

class ProfilePermission(permissions.BasePermission):
    
    message = 'Recurso no permitido.'
    admin = 'Administrador'

    def has_permission(self, request, view):

        if resolve(request.path_info).url_name == 'main-dependencia' and self.admin in request.profiles:
            if request.method == 'GET' or request.method == 'POST':
                return True

        return False
