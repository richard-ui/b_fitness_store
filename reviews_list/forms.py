from django import forms
from .models import Reviews_list
from products.models import Product
from django.forms import TextInput, Textarea


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews_list
        fields = (
            "product",
            "review",
            "rating",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'product': 'Product...',
            'review': 'add review...',
            'rating': '1-5...',
        }
        self.fields['product'].widget.attrs['autofocus'] = True

        self.fields['review'].widget = Textarea(attrs={'cols': 50, 'rows': 5})

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
