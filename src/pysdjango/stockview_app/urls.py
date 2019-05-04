from django.urls import path

from . import views

urlpatterns = [
	path('', views.home_fbv, name='home_fbv'),
]