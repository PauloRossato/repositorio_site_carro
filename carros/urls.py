from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^carros$', views.index),
    url(r'^(?P<carro_id>[0-9]+)/$', views.detail),
    url(r'^fabric/$', views.Fabricante)
]
