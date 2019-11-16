from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def eng(request):
    return HttpResponse("<h1>hello from english</h1>")