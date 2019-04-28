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
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
	# mesages.debug
	# messages.info
	# messages.success
	# messages.warning
	# messages.error

# =============================================================================
# 3 | Registration View
# =============================================================================
def register(request):
	form = None

	if request.method == 'GET':
		form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save() # TODO: Research DJango security features
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!') # Note f string usage
			# Redirect to another page to prevent multiple re-submission of form
			return redirect('users_app:user-home')

	return render(request, 'users_app/register.html', {'form' : form})

def temp_home(request):
	return render(request, 'users_app/base.html')