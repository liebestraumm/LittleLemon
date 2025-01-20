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
    
    # def test_getall(self):
    #     # Create a user. This user is only visible to the test case
    #     user = User.objects.create_user(username="test", password="test")
    #     # Create a token programatically for the user
    #     token = Token.objects.create(user=user)
    #     self.client = Client(HTTP_AUTHORIZATION=f"Token {token.key}")
    #     # Get the Endpoint from the viewname (In this case, the viewname is menu-items, which maps to the MenuItemView class)
    #     # url = reverse('appraisal-detail', kwargs={'pk': some_pk}) -- Use this if the view has a parameter, like an ID.
    #     url = reverse("menu-items")
    #     response = self.client.get(url, format="json")

    #     # Get all Menu objects
    #     menu = MenuItem.objects.all()
    #     # Serialize the menu objects
    #     serializer = MenuItemSerializer(menu, many=True)
    #     # Check if the response data is equal to the serialized data
    #     self.assertEqual(response.data, serializer.data)



