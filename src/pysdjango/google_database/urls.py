from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

app_name = "google_database"

urlpatterns = [
    path('', views.index, name=app_name),
]