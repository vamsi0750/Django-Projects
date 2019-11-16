from django.urls import path
from . import views

urlpatterns=[
    path('vamsi/',views.vamsiView.as_view(),name="vamsi")
]
