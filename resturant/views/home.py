from django.views.generic import TemplateView
from resturant.models.item import Item
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        context = {'items': items}
        return render(request, 'home.html', context)
    
