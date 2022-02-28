from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.website,name='website'),
    path('shop/',views.index,name='index'),
]