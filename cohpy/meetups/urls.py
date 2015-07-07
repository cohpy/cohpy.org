from django.conf.urls import patterns, url

from meetups import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
