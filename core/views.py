from django.shortcuts import render
from django.http import HttpResponse

def website(request):
    return render(request, 'website.html')

def index(request):
    return render(request, 'index.html')


