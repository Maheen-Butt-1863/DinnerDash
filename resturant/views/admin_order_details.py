from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import View

from resturant.models import Order


class AdminOrderDetailsView(LoginRequiredMixin, View):
    template_name = "admin_order_details.html"

    def get(self, request, *args, **kwargs):
        status_filter = request.GET.get("status")
        if status_filter:
            orders = Order.objects.filter(in_process=False, status=status_filter)

        elif "order_pk" in request.GET:
            order_pk = request.GET["order_pk"]
            order = get_object_or_404(Order, in_process=False, pk=order_pk)
            order_items = order.orderitem_set.all()

            return render(
                request,
                self.template_name,
                {"order": order, "order_items": order_items},
            )
        else:
            orders = Order.objects.filter(in_process=False)

        return render(request, self.template_name, {"orders": orders})
