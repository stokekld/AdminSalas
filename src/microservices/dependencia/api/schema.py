from graphene_mongo import MongoengineObjectType
from .models import Dependencia
import graphene, logging

class DependenciaType(MongoengineObjectType):
    class Meta:
        model = Dependencia

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
    dependencias = graphene.List(DependenciaType, filter=FilterInput())

    def resolve_dependencias(self, info, **kwargs):
        filter = kwargs.get('filter')

        if filter is not None:
            return Dependencia.objects(**filter.input)

        return Dependencia.objects.all()
    
schema = graphene.Schema(query=Query)
