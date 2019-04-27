"""	Google API Demo Example View
	The View that generates the HTML content to be served to the browser.
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
# DJango imports
from django.urls import path

# Local imports FBV vs CBV
from .views import QueryView
from .views import dashboard as dashboard_fbv

# =============================================================================
# 3 | Define URLConf
# =============================================================================
# Application namespace
app_name = 'query_api_dashboard'

urlpatterns = [
	path('fbv', dashboard_fbv, name='query_fbv'),
	path('', QueryView.as_view(), name='query_cbv'),
]