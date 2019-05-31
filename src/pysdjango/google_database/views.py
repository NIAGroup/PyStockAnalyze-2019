from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .googleapi import CSEQuery
from .forms import Search
from .parsedata import *

class Home(TemplateView):
    template_name = 'google_database/index.html'

    def __init__(self):
        pass

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        inputText = request.POST.get('inputText')
        outputText  = ""
        #outputText, tmp = CSEQuery.cse_format(inputText)
        p = Parse()
        outputText = p.run(inputText)
        #suma = Summary().sumText("https://www.marketwatch.com/story/intel-earnings-new-ceo-is-not-getting-a-honeymoon-period-2019-04-22")
        args = {'inputText': inputText, 'outputText': outputText}
        return render(request, self.template_name, args)

    def post_query_handler(request):
        pass
