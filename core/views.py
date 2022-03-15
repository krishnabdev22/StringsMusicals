from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models.category import Category
from .models.customer import Customer
from .models.product import Product
from django.views import View

def validateCustomer(customer):
    error_message = None

    if (not customer.first_name):
        error_message = "First Name Required"
    elif len(customer.first_name) < 3:
        error_message = "First Name Must have " \
                        "Atleast 3 Character"
    if (not customer.phone):
        error_message = "Enter Your Phone Number"
    elif len(customer.phone) != 10:
        error_message = "Phone Number Not Valid"
    if (not customer.password):
        error_message = "Enter Your Password"
    elif len(customer.password) < 4:
        error_message = "Password atleast Need 4 character/numbers"
    elif customer.isExists():
        error_message = "Email Already Exists"
    return error_message

def registerUser(request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # Holding Values
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }
        # error_message = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = validateCustomer(customer)
        # Saving
        if not error_message:

            customer.password = make_password(customer.password)

            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value,

            }
            return render(request, 'signup.html', data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)


def website(request):
    return render(request, 'website.html')

def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:

        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
# ******************************* Check Password
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = email
                return redirect('index')
            else:
                error_message = "Invalid Email or Password"
        else:
            error_message = "Invalid Email or Password"

        return render(request, 'login.html', {'error' : error_message})

