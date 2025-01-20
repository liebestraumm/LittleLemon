from django.test import TestCase
from restaurant.models import MenuItem
# Create your tests here.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price = 80, inventory = 100)
        item = item.__str__()
        self.assertEqual(item, "IceCream : 80")