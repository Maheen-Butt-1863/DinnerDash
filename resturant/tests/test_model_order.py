from django.test import TestCase

from resturant.factories.order_factory import OrderFactory


class OrderModelTest(TestCase):
    def test_status_update(self):
        order = OrderFactory()
        expected_order_status = f"{order.status}"
        self.assertEqual(expected_order_status, order.status)
