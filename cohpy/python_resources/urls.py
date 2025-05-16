from django.urls import path

from python_resources import views

urlpatterns = [
    path('', views.index, name='index'),
]
