from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#Hi guys

def home(request):
    #return HttpResponse("Home Page")
    return render(request, 'home.html')