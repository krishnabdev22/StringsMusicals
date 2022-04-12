from django.shortcuts import redirect
from django.views import View
from ..models.customer import Customer
from ..models.orders import Order
from ..models.product import Product
from django.contrib import messages



class Checkout(View):
    def post(self, request):
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
            messages.info(request, 'Your Order is Placed Successfully')
        request.session['cart'] = {}
        print(name, address, phone, customer, cart, products)
        return redirect('cart')
