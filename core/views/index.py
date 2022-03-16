from django.shortcuts import render
from ..models.category import Category
from ..models.product import Product

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