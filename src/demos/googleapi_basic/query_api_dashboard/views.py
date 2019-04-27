from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse

from query_api_dashboard.forms import MainForm
from query_api_dashboard.googleapi import CSEQuery

# Create your views here.
def dashboard(request):
	return render(request, 'query_api_dashboard/dashboard.html')


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
			form = MainForm()
		
		args = {'form' : form, 'text' : text}
		return render(request, self.template_name, args)

	def post_query_handler(request):
		pass
