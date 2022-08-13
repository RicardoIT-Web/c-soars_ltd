""" payment forms """
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Payment form content"""

    class Meta:
        """Payment form content"""

        model = Order
        fields = (
            "name",
            "email",
            "contact_number",
            "address1",
            "address2",
            "post_code",
            "city",
            "county",
            "country",
        )

    def __init__(self, *args, **kwargs):
        """
        Override init method to allow us to customize fields
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Full Name",
            "email": "Email Address",
            "contact_number": "Contact Number",
            "address1": "Address Line 1",
            "address2": "Address Line 2",
            "post_code": "Post Code",
            "city": "City",
            "county": "County",
        }

        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False
