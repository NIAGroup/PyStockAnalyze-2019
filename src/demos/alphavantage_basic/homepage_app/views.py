from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .scripts.homepage_app.test_alphavantage_crypto import Crypto_Generate, AlphaInputs

# Create your views here.
#Hi guys

def home(request):
    #return HttpResponse("Home Page")
    return render(request, 'homepage_app/home.html')

def get_dropdown_options(request,*args,**kwargs):
	alphainputs = AlphaInputs()
	symbols = alphainputs.get_crypto_symbols()
	markets = alphainputs.get_crypto_markets()  
	ops = {
	"symbols" : symbols,
	"markets" : markets,
	}
	return JsonResponse(ops)

def testing(request,*args,**kwargs):

	symbol = request.GET.get('symbol')
	symbol = symbol.split(" : ")
	symbol = symbol[0]
	market = request.GET.get('market')
	cry_g = Crypto_Generate()
	vals = cry_g.get_daily(symbol,market)
	return JsonResponse(vals)

