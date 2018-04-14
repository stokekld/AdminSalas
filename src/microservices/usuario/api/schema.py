from graphene_mongo import MongoengineObjectType
from .models import Datos, Usuario
import graphene, logging

class DatosType(MongoengineObjectType):
    class Meta:
        model = Datos

class UsuarioType(graphene.ObjectType):
    id = graphene.String()
    datos = graphene.Field(DatosType)
    dependencia = graphene.String()
    perfiles = graphene.List(graphene.String)
    user= graphene.String()
    password = graphene.String()
    activo = graphene.Boolean()

class FilterInput(graphene.InputObjectType):
    id = graphene.String(default_value=None)

    @property
    def input(self):
        aux_list = {}
        for key in self.__dict__.keys():
            if self.__dict__[key] is not None:
                aux_list[key] = self.__dict__[key]

        return aux_list

class Query(graphene.ObjectType):
    usuarios = graphene.List(UsuarioType, filter=FilterInput())

    def resolve_usuarios(self, info, **kwargs):
        filter = kwargs.get('filter')

        if filter is not None:
            return Usuario.objects(**filter.input)

        return Usuario.objects.all()

schema = graphene.Schema(query=Query)
