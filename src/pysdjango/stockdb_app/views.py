from django.shortcuts import render

# Create your views here.
def home_fbv(request):
	return render(request, 'stockdb_app/base.html')