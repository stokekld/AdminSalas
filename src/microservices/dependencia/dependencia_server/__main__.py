#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Esta es la primera versión de la api del microservicio de Dependencia'})
    app.run(port=8080)
