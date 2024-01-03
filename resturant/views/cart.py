from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from resturant.forms.update_cart import AddToCartForm
from resturant.models.item import Item
from resturant.models.order import Order
from resturant.models.orderitem import OrderItem


class CartPageView(TemplateView):
    template_name = "cart.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

        cart = Order.get_cart(user)
        cart_items = cart.orderitem_set.all()
        item_details = []
        for item in cart_items:
            item_details.append(
                {
                    "item_id": item.item.id,
                    "name": item.item.title,
                    "price": item.item.price,
                    "quantity": item.quantity,
                    "sub_total": item.quantity * item.item.price,
                }
            )
        total_price = sum(item["quantity"] * item["price"] for item in item_details)

        return render(
            request,
            "cart.html",
            {"item_details": item_details, "total_price": total_price},
        )

    def post(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        form = AddToCartForm(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data["item_id"]
            item = get_object_or_404(Item, pk=item_id)
            cart = Order.get_cart(user)
            order_item, created = OrderItem.objects.get_or_create(order=cart, item=item)
            action = form.cleaned_data.get("action")

            if action == "remove":
                order_item.delete()
            elif action == "update" and form.cleaned_data.get("quantity"):
                order_item.quantity = form.cleaned_data["quantity"]
                order_item.save()
            elif not created:
                order_item.quantity += 1
                order_item.save()

            cart.refresh_from_db()

            return redirect("cart")

        else:
            return redirect("home")
