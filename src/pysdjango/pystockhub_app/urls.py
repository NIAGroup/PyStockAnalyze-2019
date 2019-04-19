from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

app_name = "pystockhub_app"

urlpatterns = [
    path('', views.disp_index, name=app_name),
]