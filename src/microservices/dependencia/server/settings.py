"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from mongoengine import connect
import os, logging, mongoengine

logging.basicConfig(level=logging.INFO)

if 'DB_HOST' in os.environ and 'DB_NAME' in os.environ:
    connect(os.environ['DB_NAME'], host=os.environ['DB_HOST'])

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['JWT_KEY'] if 'JWT_KEY' in os.environ else ""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if 'DEBUG' in os.environ and os.environ['DEBUG'] == "True" else False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'api'
]

MIDDLEWARE = [
    'middlewares.auth.Auth'
]

REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}

ROOT_URLCONF = 'server.urls'


WSGI_APPLICATION = 'server.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

