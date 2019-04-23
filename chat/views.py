from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    print("XXXXXXXXXX__Debug__XXXXXXXXXXX")
    return render(request, "home.html")