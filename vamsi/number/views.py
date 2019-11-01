from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
    return HttpResponse('<h1>first</h1>')


def Home_view(request):
    return HttpResponse('<h1>welcome to vamsi django traning</h1>')

def second_view(request):
    return HttpResponse('<h1>2</h1>')

def there_view(request):
    return HttpResponse('<h1>3</h1>')    

def four_view(request):
    return HttpResponse('<h1>4</h1>')

def five_view(request):
    return HttpResponse('<h1>5</h1>')             