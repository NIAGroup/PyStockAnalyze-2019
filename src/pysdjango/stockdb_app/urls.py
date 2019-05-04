from django.urls import path

from . import views

app_name='stockdb_app'

urlpatterns = [
	path('', views.home_fbv, name='stockdb_app:home_fbv'),
]