from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "home"

urlpatterns = [
    path('', views.home, name=app_name),
    path('tester', views.testing, name='testing_fxn'),
]