from django.shortcuts import render
from testdb.models import Emp

# Create your views here.
def emp_info(request):
    employees=Emp.objects.all()
    return render(request,'hello.html',{"emps":employees})

