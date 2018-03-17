from .models import Dependencia
import graphene

class DependenciaSchema(graphene.ObjectType):
    id = graphene.String()
    nombre = graphene.String() 
    siglas = graphene.String()

class Query(graphene.ObjectType):
    dependencia = graphene.List(DependenciaSchema)

    def resolve_dependencia(self, info):
        return Dependencia.objects.all()

schema = graphene.Schema(query=Query)
