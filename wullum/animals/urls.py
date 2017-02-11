from django.conf.urls import url

from . import views

app_name = 'animals'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all/$', views.all, name='all'),
    url(r'^dead/$', views.dead, name='dead'),
    url(r'^rabbits/$', views.rabbits, name='rabbits'),
    url(r'^chickens/$', views.chickens, name='chickens'),
    url(r'^(?P<animal_name_slug>[\w\-]+)/$', views.animal, name='animal'),
]
