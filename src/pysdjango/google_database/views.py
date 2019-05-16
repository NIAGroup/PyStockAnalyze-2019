from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .googleapi import CSEQuery
from .forms import Search

class Home(TemplateView):
    template_name = 'google_database/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        inputText = request.POST.get('inputText')
        outputText = CSEQuery.cse_format(inputText)
        inputText = ""  # Reset form input

        args = {'inputText': inputText, 'outputText': outputText}
        return render(request, self.template_name, args)

    def post_query_handler(request):
        pass
