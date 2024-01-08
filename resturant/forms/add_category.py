from django import forms
from resturant.models import Category


class CategoryAdmin(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
        ]
        
    def clean_name(self):
        name = self.cleaned_data.get('name')

        if Category.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError('A category with this name already exists.')

        return name
