from django.shortcuts import render, redirect
from django.views import View
from ..models.customer import Customer
from ..models.orders import Order
from ..models.product import Product


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        orders = orders.reverse()
        return render(request, 'orders.html', {'orders' : orders})