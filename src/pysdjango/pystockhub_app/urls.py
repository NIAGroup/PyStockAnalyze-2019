from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views


app_name = "home"

urlpatterns = [
    path('', views.home, name=app_name),
]
