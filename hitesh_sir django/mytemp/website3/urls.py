from django.urls import path
from . import views

urlpatterns=[
    path('vinay/',views.vinay.as_view(),name="vinay")
]