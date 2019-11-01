from django.urls import path
from number import views

urlpatterns = [
    path('first/',views.first_view),
    path('second/',views.second_view),
    path('3/',views.there_view),
    path('4/',views.four_view),
    path('5/',views.five_view),
    path('/',views.Home_view)


]
