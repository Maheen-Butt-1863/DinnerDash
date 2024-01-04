from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from resturant.forms import ItemForm
from resturant.models import Item


class ItemUpdateView(View):
    template_name = "update_items.html"

    def get(self, request, *args, **kwargs):
        item_id = request.GET.get("item_id")
        form = ItemForm()

        if item_id:
            item = get_object_or_404(Item, id=item_id)
            form = ItemForm(instance=item)

        return render(request, self.template_name, {"form": form, "item_id": item_id})

    def post(self, request, *args, **kwargs):
        item_id = request.POST.get("item_id")

        if item_id is not None and item_id != "None":
            item = get_object_or_404(Item, id=item_id)
            form_instance = ItemForm(request.POST, request.FILES, instance=item)

            if form_instance.is_valid():
                form_instance.save()
                messages.success(request, "Item successfully updated.")
                return redirect('home')
            else:
                return render(
                    request, self.template_name, {"form": form_instance, "item_id": item_id}
                )
        else:
            form_instance = ItemForm(request.POST, request.FILES)

            if form_instance.is_valid():
                form_instance.save()
                messages.success(request, "Item successfully added.")
                return redirect('home')
            else:
                return render(
                    request, self.template_name, {"form": form_instance, "item_id": item_id}
                )