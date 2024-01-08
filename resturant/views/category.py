import pdb

from django import forms
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from resturant.forms.add_category import CategoryAdmin
from resturant.models import Category


class CategoryUpdate(View):
    def get(self, request, *args, **kwargs):
        form = CategoryAdmin()
        return render(request, "add_category.html", {"form": form})

    def post(self, request, *args, **kwargs):

        form_instance = CategoryAdmin(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            messages.success(request, "Category successfully added.")
            return render(request, "add_category.html", {"form": form_instance})

        else:
            print(form_instance)
            return render(request, "add_category.html", {"form": form_instance})
