from django.conf.urls import url

from . import views

app_name = 'animals'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all/$', views.all, name='all'),
    url(r'^dead/$', views.dead, name='dead'),
    url(r'^rabbits/$', views.rabbits, name='rabbits'),
    url(r'^chickens/$', views.chickens, name='chickens'),
    url(r'^goats/$', views.goats, name='goats'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^(?P<animal_name_slug>[\w\-]+)/$', views.animal, name='animal'),
]
