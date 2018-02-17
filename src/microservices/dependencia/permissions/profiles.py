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
        elif resolve(request.path_info).url_name == 'id-dependencia':
            if request.method == 'PUT' or request.method == 'DELETE':
                if self.admin in request.profiles:
                    return True
            elif request.method == 'GET':
                return True

        return False
