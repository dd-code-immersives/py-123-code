from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('userdetails/',views.userDetails, name="user_details"),
    path('display/',views.userDetails, name="display"),
  	path('', admin.site.urls)
]