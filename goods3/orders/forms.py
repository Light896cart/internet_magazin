from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    phoneNumber = forms.CharField(max_length=12, min_length=11)
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phoneNumber', 'address', ]