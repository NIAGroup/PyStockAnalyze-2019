from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#Hi guys

def home(request):
    #return HttpResponse("Home Page")
    return render(request, 'homepage_app/home.html')

def testing(request,*args,**kwargs):

	print(request.GET.get('texter'))
	return render(request, 'homepage_app/home.html')

