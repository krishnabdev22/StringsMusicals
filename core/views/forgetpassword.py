from django.shortcuts import redirect,render
from django.core.mail import send_mail
from django.contrib import messages
from ..models.customer import Customer
# from Musicals.Musicals.settings import EMAIL_HOST_USER
from django.conf import settings


def forgetpass(request):
    if request.method=="POST":
        email = request.POST['email']
        users = Customer.objects.filter(email=email)
        l = len(users)
        if l == 1:
            pas = Customer.objects.get(email=email)

            subject = 'PASSWORD RESETING FOR STRINGS MUSICALS'
            message = "Your Password is : " + pas.password
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
            return redirect('login')
        else:
            messages.success(request, 'Email_id does not exists')
            return redirect('forgetpassword')
    return render(request,'forgetpassword.html')