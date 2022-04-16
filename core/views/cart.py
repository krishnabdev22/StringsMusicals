from django.shortcuts import render,redirect
from django.views import View
from ..models.customer import Customer
from ..models.product import Product
from django.views.decorators.csrf import csrf_exempt
import razorpay

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
        # Razorpay

        if request.method == "POST":


            name = request.POST.get('name')
            amount = 50000
            order_currency = 'INR'

            client = razorpay.Client(
                auth=("", ""))

            payment = client.order.create({'amount': amount, 'currency': 'INR',
                                           'payment_capture': '1'})


        # Razorpay End

        return redirect(request.META['HTTP_REFERER'])

    # @csrf_exempt
    # def success(self, request):
    #     # return redirect(request.META['HTTP_REFERER'])
    #
    #     return redirect('checkout')

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

