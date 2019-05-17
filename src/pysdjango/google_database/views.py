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
        outputText,tmp = CSEQuery.cse_format(inputText)

        args = {'inputText': inputText, 'outputText': outputText, 'tmp': tmp}
        return render(request, self.template_name, args)

    def post_query_handler(request):
        pass
