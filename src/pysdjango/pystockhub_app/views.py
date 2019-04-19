from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#Hi guys


def disp_index(request):
    return render(request, 'pystockhub_app/index.html')