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
        widgets = {"categories": forms.CheckboxSelectMultiple()}

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        price = cleaned_data.get("price")
        categories = cleaned_data.get("categories")

        if title is None or title.strip() == "":
            raise forms.ValidationError({"title": ["Title is required."]})

        if description is None or description.strip() == "":
            raise forms.ValidationError({"description": ["Description is required."]})

        if price is not None and price <= 0:
            raise forms.ValidationError({"price": ["Price cannot be negative."]})

        if not categories:
            raise forms.ValidationError({"categories": ["Categories are required."]})

        return cleaned_data
