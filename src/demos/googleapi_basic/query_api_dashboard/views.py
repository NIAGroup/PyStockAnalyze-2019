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
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse

# Local imports
from .forms import MainForm
from .googleapi import CSEQuery


# =============================================================================
# 3 | Simple Function Based View (FBV) Example
# =============================================================================
def dashboard(request):
	template_name = 'query_api_dashboard/dashboard.html'

	if request.method == 'GET':
		form = MainForm()
		return render(request, template_name, {'form': form})

	elif request.method == 'POST':
		form = MainForm(request.POST)
		text = ""
		if form.is_valid():
			text = form.cleaned_data['post']
			text = CSEQuery.cse_format(text)
			form = MainForm() # Reset form input

		args = {'form' : form, 'text' : text}
		return render(request, template_name, args)

	

# =============================================================================
# 4 | Simple Class Based View (CBV) Example
# =============================================================================
class QueryView(TemplateView):
	template_name = 'query_api_dashboard/dashboard.html'

	def get(self, request):
		form = MainForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = MainForm(request.POST)
		text = ""
		if form.is_valid():
			text = form.cleaned_data['post']
			text = CSEQuery.cse_format(text)
			form = MainForm() # Reset form input
		
		args = {'form' : form, 'text' : text}
		return render(request, self.template_name, args)

	def post_query_handler(request):
		pass
