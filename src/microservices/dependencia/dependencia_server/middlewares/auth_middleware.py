"""
Middlewares para el framework connexion
"""

import connexion, os, jwt, logging

DEBUG = True if os.environ.get('DEBUG', 'False') == "True" else False

def get_dataToken():
    """
    Obtiene el token desde la cabecera token.

    :return Retorna el payload
    """
    token = connexion.request.headers['token']
    return jwt.decode(token, os.environ['JWT_KEY'], algorithms='HS256')

def isActived(data):
    """
    Obtiene el valor de activo

    :return Retorna el valor de activo
    """
    return data['activo']

def isAuthorized(profiles, data):
    """
    Revisa los perfiles del usuario para
    saber si esta autorizado.

    :return Retorna un valor booleano
    """
    for profile in profiles:
        if profile in data['perfiles']:
            return True
    return False

def authentication(function):
    """
    Este es el middleware de autenticacion, revisa
    si el token es sano.

    :return Retorna error 401 si existe algun error en el token
    """
    def inner(*args, **kwargs):
        try:
            get_dataToken()
        except Exception as e:
            if DEBUG:
                logging.info(str(e))
            return "No autenticado", 401
        return function(*args, **kwargs)
    return inner

def authorization(profiles):
    """
    Este es el middleware de autorizacion, revisa
    si existen los perfiles del endpoint en el usuario

    :param profiles: Tiene los perfiles que pueden ejecutar
    :type: array
    """
    def outer(function):
        def inner(*args, **kwargs):

            # verifica si el token es sano
            try:
                data = get_dataToken()
            except Exception as e:
                if DEBUG:
                    logging.info(str(e))
                return "No autenticado", 401

            # verifica si el usuario esta activo
            try:
                actived = isActived(data)
            except Exception as e:
                if DEBUG:
                    logging.info(str(e))
                return "No autenticado", 401

            if not actived:
                return "No autorizado", 403

            # verifica los perfiles del endpoint
            # en los perfiles del usuario
            if not isAuthorized(profiles, data):
                return "No autorizado", 403

            return function(*args, **kwargs)
        return inner
    return outer

