from django.test import TestCase
from resturant.models import Category


class ItemPageViewTest(TestCase):

    def setUp(self):
        Category.objects.create(name='')