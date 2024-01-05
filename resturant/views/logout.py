from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from resturant.models import OrderItem, Order

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        self.remove_order_items(request.user)
        return super().dispatch(request, *args, **kwargs)

    def remove_order_items(self, user):
        if user.is_authenticated:
            user_order = Order.get_cart(user)
            OrderItem.objects.filter(order=user_order).delete()
