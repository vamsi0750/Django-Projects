from django.shortcuts import render
import datetime

# Create your views here.

def wish(request):
    date=datetime.datetime.now()
    msg="Hello root very good"
    h=int(date.strftime('%H'))
    if h<12:
        msg=msg+'Morning'
    elif h<16:
        msg=msg+'Afternoon'
    elif h<21:
        msg=msg+'Evening'

    else:
        msg=msg+'Night' 
    return render(request,'hello.html',{'msgg': msg,'dateey':date})           