"""pysdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('home/', include('homepage_app.urls'), name='home_view'),
    path('stock/view/', include ('stockview_app.urls'), name='stock_view'),
    path('stock/db/', include ('stockdb_app.urls'), name='stock_database'),
    path('google_database/', include('google_database.urls'), name='google_db'),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('pystockhub_app.urls'), name='index'),
]

=======

]

#urlpatterns += staticfiles_urlpatterns()
>>>>>>> develop
