from rest_framework.views import APIView
from rest_framework.response import Response

class MenuItemListView(APIView):
    """
    View to return a list of hardcoded menu items.
    Later,this will be replaced with database queries.

    """

    def get(self,request):
        #Hardcoded menu items for now
        menu_items=[
            {"id":1,"name":"Margherita Pizza","price":8.99},
            {"id":2,"name":"Veggie Burger","price":6.49},
            {"id":3,"name":"Pasta Alfredo","price":7.99},
        ]
        return Resonse(menu_items)