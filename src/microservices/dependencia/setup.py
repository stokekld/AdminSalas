# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "dependencia_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Dependencia",
    author_email="jesusflores@unam.mx",
    url="",
    keywords=["Swagger", "Dependencia"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    Esta es la primera versión de la api del microservicio de Dependencia
    """
)

