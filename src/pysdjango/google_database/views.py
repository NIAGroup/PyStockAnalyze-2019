from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('google_database/index.html')
    context = {

    }
    return HttpResponse(template.render(context,request))
