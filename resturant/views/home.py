from django.shortcuts import render
from django.views.generic import TemplateView

from resturant.models.category import Category
from resturant.models.item import Item


class HomePageView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        category_id = request.GET.get("category_id")
        print(category_id)
        if category_id:
            try:
                category_id = int(category_id)
                items = Item.objects.filter(categories__id=category_id)
            except ValueError:
                return render(request, "invalid_category.html")
        else:
            items = Item.objects.all()

        categories = Category.objects.all()
        context = {
            "items": items,
            "categories": categories,
            "selected_category": category_id,
        }
        return render(request, "home.html", context)
