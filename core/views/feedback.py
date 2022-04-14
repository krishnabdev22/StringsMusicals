from ..models.feedback import Feedback
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

def feed(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print('................', name)
        email = request.POST.get('email')
        feed = request.POST.get('feed')
        feeback = Feedback(name=name,
                           email=email,
                           feed=feed)

        feeback.save();
        messages.info(request,'Thankyou For Your Valuable Feedback')
        # messages.info(request, 'Thankyou For Your,');
        return redirect('website')
