"""	User application URL Configuration
	The URL configuration for the user application.
"""

# =============================================================================
# 1 | Document Metadata
# =============================================================================
__author__    = 'Lennard Streat'
__copyright__ = 'Network of Intel African Americans 2019, PyStockAnalyze Project'
__credits__   = ['Lennard Streat', 'Princton Brennan']
__license__   = 'MIT'
__version__   = '1.0'
__email__     = 'nia.stem.club'

# =============================================================================
# 2 | Imports
# =============================================================================
from django.urls import path
from . import views


# =============================================================================
# 3 | Define URLConf
# =============================================================================
# Application namespace
app_name = 'users_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.temp_home, name='user-home'),
]