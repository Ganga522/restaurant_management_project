from django.http.import JsonResponse
from rest_framework import APIView

# Create your views here.
class MenuItemListView(APIView):
    def get(self,request):
        menu_items=[
            {"id":1,"name":"Margherita Pizza","price":8.99},
            {"id":2,"name":"Veggie Burger","price":6.49},
            {"id":3,"name":"Pasta Alfredo","price":7.99},
        ]
        return JsonResponse(menu_items,safe=False)