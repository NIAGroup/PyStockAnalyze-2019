from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .forms import SearchForm
from .googleapi import CSEQuery

class Home(TemplateView):
	template_name = 'google_database/index.html'

	def get(self, request):
		inputText = SearchForm()
		return render(request, self.template_name, {'inputText': inputText})

	def post(self, request):
		inputText = SearchForm(request.POST)
		outputText = ""
		if inputText.is_valid():
			outputText = inputText.cleaned_data['post']
			outputText = CSEQuery.cse_format(outputText)
			inputText = SearchForm() # Reset form input
		
		args = {'form' : inputText, 'outputText' : outputText}
		return render(request, self.template_name, args)

	def post_query_handler(request):
		pass
