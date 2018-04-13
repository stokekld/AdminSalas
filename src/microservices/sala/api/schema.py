from graphene_mongo import MongoengineObjectType
from .models import Sala
import graphene, logging

class SalaType(MongoengineObjectType):
    class Meta:
        model = Sala

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
    salas = graphene.List(SalaType, filter=FilterInput())

    def resolve_salas(self, info, **kwargs):
        filter = kwargs.get('filter')

        if filter is not None:
            return Sala.objects(**filter.input)

        return Sala.objects.all()

schema = graphene.Schema(query=Query)
