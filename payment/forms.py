from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email', 'contact_number',
                  'address1', 'address2', 'post_code',
                  'city', 'county', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Override init method to allow us to customise fields
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'contact_number': 'Contact Number',
            'address1': 'Address Line 1',
            'address2': 'Address Line 2',
            'post_code': 'Post Code',
            'city': 'City',
            'county': 'County',
            'Country': 'Country',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
