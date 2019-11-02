from django.shortcuts import render
import datetime
# Create your views here.
def vamsi_view(request):
    dt=datetime.datetime.now()
    dd=datetime.datetime.now()
    name='vamsi'
    roll=1233
    branch='IT'
    my_dict={'date':dt,'va':dd,'name':name,'roll':roll,'branch':branch}

    return render(request,'v1/hello.html',context=my_dict)

     