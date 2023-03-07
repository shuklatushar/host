from django.contrib import admin
from django.urls import path
from .views import index,result,contact,home,aboutus

urlpatterns = [
    path('',index),
    path('result',result),
    path('contact',contact),
    path('home',home),
    path('aboutus',aboutus)
]