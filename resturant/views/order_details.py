from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import View

from resturant.models import Order


class OrderDetailsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if "order_pk" in request.GET:
            order_pk = request.GET["order_pk"]
            order = get_object_or_404(Order, user=user, in_process=False, pk=order_pk)
            order_items = order.orderitem_set.all()

            return render(
                request, "checkout.html", {"order": order, "order_items": order_items}
            )

        else:
            orders = Order.objects.filter(user=user, in_process=False)
            return render(request, "checkout.html", {"orders": orders})

    def post(self, request, *args, **kwargs):
        cart = Order.objects.filter(user=request.user, in_process=True).first()

        total_price_str = request.GET.get("total_price")
        if total_price_str:
            total_price = Decimal(total_price_str)
            if total_price > Decimal("0.0"):
                cart.order_total = total_price
                cart.in_process = False
                cart.save()

                return redirect("order_details")

        messages.warning(request, "No items in the cart.")
        return redirect(reverse("cart"))
