from django.urls import path
from home import views
from django.shortcuts import HttpResponse 


urlpatterns = [
    path('',views.home, name = 'home'),
    path('www.instagram.com/shubh.01123',views.home, name = 'insta')
    


]
