from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name='homepage'),
    path('contact/',views.contact_view,name='contact'),
]