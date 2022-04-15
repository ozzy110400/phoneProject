from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_phone', views.add_phone, name='add_phone'),
]
