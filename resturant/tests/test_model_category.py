from django.test import TestCase

from resturant.factories.category_factory import CategoryFactory


class CategoryModelTest(TestCase):
    def test_name_insertion(self):
        category = CategoryFactory()
        expected_object_name = f"{category.name}"
        self.assertEqual(expected_object_name, category.name)
