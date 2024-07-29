# forms.py
from django import forms
from pricing.models import Customer, Product, Offer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'
