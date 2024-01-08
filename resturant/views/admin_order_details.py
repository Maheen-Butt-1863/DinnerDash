from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import View

from resturant.models import CustomUser, Order


class AdminOrderDetailsView(LoginRequiredMixin, View):
    template_name = "admin_order_details.html"

    def get(self, request, *args, **kwargs):
        # breakpoint()
        status_filter = request.GET.get("status")
        if status_filter:
            orders = Order.objects.filter(in_process=False, status=status_filter)

        elif "order_pk" in request.GET:
            order_pk = request.GET["order_pk"]
            order = get_object_or_404(Order, in_process=False, pk=order_pk)
            user_info = get_object_or_404(CustomUser, pk=order.user.id)
            order_items = order.orderitem_set.all().annotate(
                sub_total=F("quantity") * F("item__price")
            )
            context = {
                "order": order,
                "order_items": order_items,
                "user_info": user_info,
            }

            return render(request, self.template_name, context)
        else:
            orders = Order.objects.filter(in_process=False)

        return render(request, self.template_name, {"orders": orders})

    def post(self, request, *args, **kwargs):
        order_pk = request.POST.get("order_pk")
        order = get_object_or_404(Order, in_process=False, pk=order_pk)
        action = request.POST.get("action")

        if action == "cancel":
            order.status = "cancelled"
            order.action_timestamp = timezone.now()
        elif action == "paid":
            order.status = "paid"
        else:
            order.status = "completed"
            order.action_timestamp = timezone.now()

        order.save()

        return redirect("admin_order_details")
