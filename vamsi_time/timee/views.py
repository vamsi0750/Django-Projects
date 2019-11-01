import datetime
from django.http import HttpResponse

# Create your views here.
def date_time_n(request):
    date=datetime.datetime.now()
    s="<h1>current time is " , str(date) 
    return  HttpResponse(s)
def vamsi(request):
    return HttpResponse("vamsi")   

