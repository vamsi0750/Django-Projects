from django.shortcuts import render

from django.http import HttpResponse

# Create your tests here.
def hh(request):
    return HttpResponse("Hello from Telugu")