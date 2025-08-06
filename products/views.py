from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_menu(request):
    menu=[
        {
            "name":"Pizza",
            "description":"Classic cheese and tomato pizza with fresh basil.",
            "price":250
        },
        {
            "name":"Paneer Butter Masala",
            "description":"Cottage cheese in a creamy tomato gravy",
            "price":180
        },
        {
            "name":"Veg Biryani",
            "description":"Aromatic basmati rice with mixed vegetables and spices.",
            "price":200
        },
    ]
    return Response(menu)