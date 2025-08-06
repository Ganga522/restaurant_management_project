import requests
from django.shortcuts import render

# Create your views here.

def homepage(request):
    response=requests.get('http://localhost:8000/api/products/menu/')
    menu=response.json() if response.status_code == 200 else []
    return render(request,'home/index.html',{'menu':menu})
