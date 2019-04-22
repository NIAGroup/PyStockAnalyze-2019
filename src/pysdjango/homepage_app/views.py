from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .scripts.homepage_app.test_alphavantage_crypto import Crypto_Generate

# Create your views here.
#Hi guys

def home(request):
    #return HttpResponse("Home Page")
    return render(request, 'homepage_app/home.html')

def testing(request,*args,**kwargs):

	symbol = request.GET.get('symbol')
	market = request.GET.get('market')
	cry_g = Crypto_Generate()
	print("running")
	vals = cry_g.get_daily(symbol,market)
	return JsonResponse(vals)

