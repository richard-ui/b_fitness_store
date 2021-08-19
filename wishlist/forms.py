from django import forms
from .models import Wishlist
from products.models import Product
from django.forms import TextInput, Textarea


class WishlistForm(forms.ModelForm):

    class Meta:
        model = Wishlist
        fields = (
            "products",
            "name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'product': 'Product...',
            'name': 'name',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
