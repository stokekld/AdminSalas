from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'v1/dependencia/$', views.MainView.as_view(), name='main-dependencia'),
    url(r'v1/dependencia/(?P<id>[0-9a-z]+)$', views.IdView.as_view(), name='id-dependencia')
]

