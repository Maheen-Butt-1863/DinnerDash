from django import forms

from resturant.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "title",
            "description",
            "price",
            "is_available",
            "photo",
            "categories",
        ]
        widgets = {
            "categories": forms.CheckboxSelectMultiple(),
        }
