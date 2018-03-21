from graphene_mongo import MongoengineObjectType
from .models import Dependencia
import graphene, logging

class DependenciaType(MongoengineObjectType):
    class Meta:
        model = Dependencia

class Query(graphene.ObjectType):
    dependencia = graphene.Field(DependenciaType, id=graphene.String())
    dependencias = graphene.List(DependenciaType)

    def resolve_dependencia(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Dependencia.objects.get(id=id)

        return None

    def resolve_dependencias(self, info, **kwargs):
        return Dependencia.objects.all()

schema = graphene.Schema(query=Query)
