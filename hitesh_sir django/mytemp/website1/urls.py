from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.HomePage.as_view(),name="index"),
    path('about/',views.AboutPage.as_view(),name="about"),
    path('conatct/',views.ConatactPage.as_view(),name="contact"),


    
]
