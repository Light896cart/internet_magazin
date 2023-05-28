from django import forms

# from main.models import ProductSizes


# class CartAddProductForm(forms.Form):
#     update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
#     override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
class CartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)