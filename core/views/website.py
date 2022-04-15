from django.shortcuts import render
from ..models.customer import Customer
from ..models.feedback import Feedback
from ..models.category import Category
from django.views import View

class Website(View):
    def get(self,request):
        data = {}
        id = request.session.get('customer')
        if not id:
            request.session['customer'] = {}
            print("...No one is logged")
            categories = Category.get_all_categories()

            feeds = Feedback.get_all_feeds()
            data['feeds'] = feeds
            print(".........................",feeds)
        else:
            name = Customer.objects.get(id=id)
            data['username'] = name.first_name
            data['email'] = name.email
            feeds = Feedback.get_all_feeds()
            data['feeds'] = feeds
            print(feeds)
        return render(request, 'website.html', data)

