from django.contrib import admin
from django.urls import path
from .views import website, index, signup, login, cart, checkout, orders
urlpatterns = [
    path('',website.website,name='website'),
    path('shop/',index.Index.as_view(),name='index'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', login.logout, name='logout'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('checkout',checkout.Checkout.as_view() , name='checkout'),
    path('orders', orders.OrderView.as_view(), name='orders')
]
