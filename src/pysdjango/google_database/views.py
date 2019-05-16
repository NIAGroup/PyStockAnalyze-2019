from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .forms import MainForm
from .googleapi import CSEQuery

class Home(TemplateView):
	template_name = 'google_database/index.html'

	def get(self, request):
		inputText = MainForm()
		return render(request, self.template_name, {'inputText': inputText})

	def post(self, request):
		inputText = MainForm(request.POST)
		outputText = ""
		if inputText.is_valid():
			outputText = inputText.cleaned_data['post']
			outputText = CSEQuery.cse_format(outputText)
			inputText = MainForm() # Reset form input
		
		args = {'form' : inputText, 'outputText' : outputText}
		return render(request, self.template_name, args)

	def post_query_handler(request):
		pass
