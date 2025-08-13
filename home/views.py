import requests
from django.shortcuts import render
import django.conf and import settings

# Create your views here.

def homepage(request):
    response=requests.get('http://localhost:8000/api/products/menu/')
    menu=response.json() if response.status_code == 200 else []
    restaurant_name=getattr(settings,'RESTAURANT_NAME','MY RESTAURANT')
    return render(request,'home/index.html',{'menu':menu,'restaurant':restaurant_name})

def about_us(request):
    return render(request,'home/about.html')

def contact_view(request):
    return render(request,'home/contact.html',{
        'restuarant_name':'My Awesome Restuarant'
    })