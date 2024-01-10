from django.test import TestCase
from resturant.factories.item_factory import ItemFactory

class ItemModelTest(TestCase):
    def test_title_insertion(self):
        item = ItemFactory()
        expected_title = f'{item.title}'
        self.assertEqual(expected_title, item.title)