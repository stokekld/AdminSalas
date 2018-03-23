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

class Query(graphene.ObjectType):
    usuarios = graphene.List(UsuarioType)

    def resolve_usuarios(self, info, **kwargs):
        return Usuario.objects.all()

schema = graphene.Schema(query=Query)
