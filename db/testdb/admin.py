from django.contrib import admin
from testdb.models import Emp


# Register your models here.
class List(admin.ModelAdmin):
    list_display=['eno','ename','esal','eadd']

admin.site.register(Emp,List)

