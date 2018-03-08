from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'v1/usuario/$', views.MainView.as_view(), name='main-usuario'),
    url(r'v1/usuario/(?P<id>[0-9a-z]{24})$', views.IdView.as_view(), name='id-usuario')
]

