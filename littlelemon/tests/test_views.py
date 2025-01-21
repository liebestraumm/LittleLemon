from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.serializers import MenuItemSerializer
from restaurant.models import MenuItem
from rest_framework.test import APIRequestFactory 


class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Pizza", price=500, inventory=50)
        MenuItem.objects.create(title="Burger", price=200, inventory=200)
        
    def test_getall(self):
        # Get response data from MenuItemView
        view = MenuItemView.as_view()
        request = APIRequestFactory().get('/items')
        response = view(request)
        # Get all Menu objects
        menu = MenuItem.objects.all()
        # Serialize the menu objects
        serializer = MenuItemSerializer(menu, many=True)
        # Check if the response data is equal to the serialized data
        self.assertEqual(response.data, serializer.data)