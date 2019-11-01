from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>welcome to Home page</h1>")

def login(request):
    return HttpResponse("<h1>Login Hi</h1>")

def logout(request):
    return HttpResponse("<h1>Logout</h1>")    
def Hola(request):
        return HttpResponse("<h1>Hola means nameste in telugu</h1>")    


