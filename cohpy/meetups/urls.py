from django.urls import path

from meetups import views

urlpatterns = [
    path('', views.index, name='index'),
]
