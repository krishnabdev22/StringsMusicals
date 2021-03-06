from django.shortcuts import render, redirect
from ..models.category import Category
from ..models.product import Product
from ..models.customer import Customer
from django.views import View


class Index(View):

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
        return redirect('index')

    def get(self, request):
        cart = request.session.get('cart')
        data = {}
        if not cart:
            request.session['cart'] = {}
        products = None
        # request.session.get('cart').clear()
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        id = request.session.get('customer')
        if not id:
            request.session['customer'] = {}
            print("...No one is logged")
        else:
            print("..............", id)
            name = Customer.objects.get(id=id)
            data['username'] = name.first_name
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:

            products = Product.get_all_products()
        # print(products)

        #
        # print("Name : ",name.first_name)
        data['products'] = products
        data['categories'] = categories
        # data['username'] = name.first_name
        # username = Customer.objects.all()
        # print("..............",username)
        print('you are :', request.session.get('email'))
        return render(request, 'index.html', data)

