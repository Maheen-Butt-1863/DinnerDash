from django import forms


class AddToCartForm(forms.Form):
    item_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1, required=False)
    remove = forms.BooleanField(required=False)
    action = forms.CharField(widget=forms.HiddenInput(), required=False)
