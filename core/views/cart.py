from django.shortcuts import render,redirect
from django.views import View
from ..models.customer import Customer
from ..models.product import Product



class Cart(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart : ', request.session['cart'])
        return redirect(request.META['HTTP_REFERER'])

    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        # id = request.session.get('customer')
        # name = Customer.objects.get(id=id)
        data={}
        # data['username'] = name.first_name
        data['products'] = products
        return render(request, 'cart.html',data)

