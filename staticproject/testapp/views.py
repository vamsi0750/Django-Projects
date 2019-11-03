from django.shortcuts import render

# Create your views here.
def img(request):
    hi="WELCOME TO VAMSI PORTAL"
    return render(request,'hello.html',{'hi':hi})