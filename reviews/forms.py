from django import forms
from .models import Review
from products.models import Product
from django.forms import TextInput, Textarea


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review'].widget = Textarea(attrs={'cols': 50, 'rows': 5})

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
