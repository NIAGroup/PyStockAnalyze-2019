from django.urls import path

#from . import views
from query_api_dashboard.views import QueryView
app_name = 'query_api_dashboard'

urlpatterns = [
	#path('', views.dashboard, name=app_name),
	#path('create_post', QueryView.post_query_handler, name='query_handler'),
	path('', QueryView.as_view(), name=app_name),
]