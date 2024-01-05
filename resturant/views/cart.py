from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from resturant.forms.update_cart import AddToCartForm
from resturant.models.item import Item
from resturant.models.order import Order
from resturant.models.orderitem import OrderItem
from django.contrib.auth.decorators import login_required

class CartPageView(TemplateView):
    template_name = "cart.html"
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cart = Order.get_cart(request.user)
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
        else:
            session_cart = request.session.get('session_cart', [])   
            item_details = []
            for item in session_cart:
                item_details.append(
                    {
                        "item_id": item["item_id"],
                        "name": item["name"],
                        "price": item["price"],
                        "quantity": item["quantity"],  # Set default quantity for unauthenticated users
                        "sub_total": item["quantity"] * item["price"],  # Set default sub_total for unauthenticated users
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
        
            if not user: 
                session_cart = request.session.get('session_cart', [])
                print(session_cart)
                action = form.cleaned_data.get("action")

                if action == "remove":
                    index = None
                    for i, item in enumerate(session_cart):
                        if item["item_id"] ==item_id:
                            index = i
                            break
                    if index is not None:
                        session_cart.pop(index)
                        request.session["session_cart"] = session_cart
                        request.session.save()

                elif action == "update":
                    for item in session_cart:
                        if item["item_id"] ==item_id:
                            item["quantity"] = form.cleaned_data["quantity"]
                    request.session.save()
                    return redirect("cart")
                
                elif item_id not in session_cart:
                    session_cart.append({
                        "item_id": item_id,
                        "name": item.title,
                        "price": float(item.price),
                        "quantity": 1,
                    })
                    request.session["session_cart"] = session_cart
                    request.session.save()

                return redirect("cart")

            else:
                cart = Order.get_cart(user)
                order_item, created = OrderItem.objects.get_or_create(order=cart, item=item)
                action = form.cleaned_data.get("action")

                if action == "remove":
                    order_item.delete()
                    return redirect("cart")
                elif action == "update" and form.cleaned_data.get("quantity"):
                    order_item.quantity = form.cleaned_data["quantity"]
                    order_item.save()
                    return redirect("cart")
                elif not created:
                    order_item.quantity += 1
                    order_item.save()

                cart.refresh_from_db()

                return redirect("home")
        else:
            return redirect("home")
