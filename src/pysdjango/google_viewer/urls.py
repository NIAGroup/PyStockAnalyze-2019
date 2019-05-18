from django.urls import path

from . import views

app_name='google_viewer'

urlpatterns = [
	path('', views.home_fbv, name='home_fbv'),
]