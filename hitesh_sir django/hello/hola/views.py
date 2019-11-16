from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vamsi(request):
    return HttpResponse('<h1>Hola means hello in spanish</h1>')

