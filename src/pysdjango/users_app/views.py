"""	User Application View
	Serves the HTTP response content to the requesting client.
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
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# =============================================================================
# 3 | Registration View
# =============================================================================
def register(request):
	form = UserCreationForm()
	return render(request, 'users/register.html', {'form' : form})