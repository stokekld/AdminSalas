from rest_framework import permissions
import logging

class ProfilePermission(permissions.BasePermission):
    
    message = 'Recurso no permitido.'

    def has_permission(self, request, view):

        if request.method == 'GET' or request.method == 'POST':
            if request.path == '/v1/dependencia/' and 'Administrador' in request.profiles:
                return True

        return False
