from django.contrib import admin
from django.urls import path
from .views import website, index, signup, login
urlpatterns = [
    path('',website.website,name='website'),
    path('shop/',index.Index.as_view(),name='index'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
]