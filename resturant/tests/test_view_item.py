from django.test import TestCase
from django.urls import reverse

from resturant.models import Item

from ..factories.category_factory import CategoryFactory
from ..factories.item_factory import ItemFactory


class ItemPageViewTest(TestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/item/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("item"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("item"))
        self.assertTemplateUsed(resp, "update_items.html")

    def test_add_item_sucess_test(self):
        category1 = CategoryFactory.create()
        category2 = CategoryFactory.create()
        item = ItemFactory()
        form_data = {
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "is_available": item.is_available,
            "categories": [category1.id, category2.id],
        }
        url = reverse("item")
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.title, item.title)

    def test_add_item_empty_feild_failure_test(self):
        category1 = CategoryFactory.create()
        category2 = CategoryFactory.create()
        item = ItemFactory()
        form_data = {
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "is_available": item.is_available,
            "categories": "",
        }
        url = reverse("item")
        response = self.client.post(url, form_data)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["form"].is_valid())
