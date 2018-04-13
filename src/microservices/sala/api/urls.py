from graphene_django.views import GraphQLView
from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'v1/$', views.MainView.as_view(), name='main-sala'),
    url(r'v1/(?P<id>[0-9a-z]{24})$', views.IdView.as_view(), name='id-sala'),
    url(r'v1/query$', GraphQLView.as_view(graphiql=True), name='query-usuario'),
]

