from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "home"

urlpatterns = [
    path('', views.home, name=app_name),
    path('tester', views.testing, name='testing_fxn'),
    path('dropdowns', views.get_dropdown_options, name='dropdown_options'),
    path('forex', views.compare_currency, name='foreign_exchange'),
]