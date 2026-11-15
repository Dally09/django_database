from django import forms

from myapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'category', 'cost', 'price', 'discount', 'for_sale', 'pic']