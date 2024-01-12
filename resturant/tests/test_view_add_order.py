from django.test import TestCase, Client
from ..factories.order_item_factory import OrderItemFactory
from ..factories.item_factory import ItemFactory
from ..factories.user_factory import CustomUserFactory
from ..factories.order_factory import OrderFactory
from django.urls import reverse


class OrderDetailsViewTestCase(TestCase):
    def setUp(self):
        self.user = CustomUserFactory()
        self.menu_item = ItemFactory()
        self.cart = OrderFactory(user=self.user, in_process=True)
        self.order_item = OrderItemFactory(order=self.cart, item=self.menu_item)
        self.client = Client()

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/order_details/")
        self.assertEqual(resp.status_code, 302)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("order_details"))
        self.assertEqual(resp.status_code, 302)

    def test_post_order_details_with_valid_total_price(self):
        self.client.force_login(self.user)
        resp = self.client.post(reverse("order_details"), {"total_price": "20.00"})
        self.assertRedirects(resp, reverse("order_details"))
        self.cart.refresh_from_db()
        self.assertFalse(self.cart.in_process)

    def test_post_order_details_with_invalid_total_price(self):
        print("coming in this logic")
        self.client.force_login(self.user)
        resp = self.client.post(reverse("cart"), {"total_price": ""})
        self.assertRedirects(resp, ("cart"))
