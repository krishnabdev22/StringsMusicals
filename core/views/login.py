from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from ..models import Customer

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):

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

        return render(request, 'login.html', {'error': error_message})

