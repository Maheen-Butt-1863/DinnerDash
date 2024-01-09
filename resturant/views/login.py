from django.contrib.auth.views import LoginView

from resturant.models.order import Order
from resturant.models.orderitem import OrderItem


class CustomLoginView(LoginView):
    def form_valid(self, form):

        response = super().form_valid(form)

        self.move_items_from_session_to_order()

        return response

    def move_items_from_session_to_order(self):
        user = self.request.user
        session_cart = self.request.session.get("session_cart")

        if user.is_authenticated and session_cart:
            user_order = Order.get_cart(user)

            for session_item in session_cart:
                item_id = session_item["item_id"]

                order_item, created = OrderItem.objects.get_or_create(
                    order=user_order, item_id=item_id
                )
                order_item.save()

            self.request.session["cart"] = []

    def get_success_url(self):
        return "/"
