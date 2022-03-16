from django.shortcuts import render

def website(request):
    return render(request, 'website.html')
