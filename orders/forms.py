from urllib import request

from django import forms
from orders.models import Order
from users.models import User


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'sername'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'email'}))


    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email')