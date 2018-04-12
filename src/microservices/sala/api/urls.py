from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'v1/$', views.MainView.as_view(), name='main-sala'),
]

