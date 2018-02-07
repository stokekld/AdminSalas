from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'v1/dependencia/$', views.ApiView.as_view())
]

