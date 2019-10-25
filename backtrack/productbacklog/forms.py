from django import forms
from .models import Product,ProductBacklogItem, ProductBacklogItemOrder

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ( 'name',)

class AddPBIForm(forms.ModelForm):
    class Meta:
        model = ProductBacklogItem
        fields = ( 'name', 'description', 'storypoint')
