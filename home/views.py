import requests
from django.shortcuts import render
from django.conf import settings
from django.conf.urls import handler404

# Create your views here.

def homepage(request):
    response=requests.get('http://localhost:8000/api/products/menu/')
    menu=response.json() if response.status_code == 200 else []

    restaurant_name=getattr(settings,'RESTAURANT_NAME','MY RESTAURANT')
    phone_number=getattr(settings,'RESTAURANT_PHONE_NUMBER','+91 9381253610')

    return render(request,'home/index.html',{
        'menu':menu,
        'restaurant':restaurant_name,
        'phone_number':phone_number
    })

def about_us(request):
    return render(request,'home/about.html',{
        'restuarant_name':getattr(settings,'RESTAURANT_NAME','MY RESTAURANT'),
        'phone_number':getattr(settings,'RESTAURANT_PHONE_NUMBER','+91 9381253611')
    })

def contact_view(request):
    return render(request,'home/contact.html',{
        'restuarant_name':getattr(settings,'RESTUARANT','MY AWESOME Restaurant'),
        'phone_number':getattr(settings,'RESTAURANT_PHONE_NUMBER','+91 9381253611')
    })


def custom_404_view(request,exception):
    return render(request,'404.html',status=404)

handler404=custom_404_view