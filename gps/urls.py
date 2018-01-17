from django.urls import path

from gps import views

urlpatterns = [
    path('', views.index, name='index'),
]
