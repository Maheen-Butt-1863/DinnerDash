# from django.test import TestCase
# from django.urls import reverse
# from resturant.factories import CustomUserFactory, ItemFactory, OrderFactory, OrderItemFactory

# class CartPageViewTest(TestCase):
#     def setUp(self):
#         self.user = CustomUserFactory()
#         self.item = ItemFactory()

#     def test_cart_page_post_authenticated_user(self):
#         self.client.force_login(self.user)
#         cart = OrderFactory(user=self.user)
#         OrderItemFactory(order=cart, item=self.item, quantity=2)
#         url = reverse('cart')
#         form_data = {'item_id': self.item.pk, 'action': 'remove'}
#         response = self.client.post(url, data=form_data)
#         self.assertEqual(response.status_code, 302) 

    