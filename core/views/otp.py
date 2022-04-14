from django.shortcuts import render, redirect

from ..models.customer import Customer
from django.contrib import messages


def otpVerify(request, email):
    print("-----------------------------")
    if request.method == "POST":
        user_entry = request.POST['userentry']
        customer = Customer.objects.get(email=email)
        print("-----------------------------", email)
        print("-----------------------------", user_entry)
        if int(user_entry) == int(customer.otp):
            print("---------------------", user_entry, customer.otp     )
            customer.otp_verified = True
            customer.save()
            messages.info(request, "registered successfully! please login")
            return redirect('login')
        else:
            messages.info(request, "invalid otp please type the 6 digit otp")
            return redirect('otpVerify_url', email)
    return render(request, 'otp.html')