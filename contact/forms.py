""" Contact Us forms """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form
    """

    class Meta:
        """contact form content"""

        model = Contact
        fields = [
            "name", "email", "contact_number",
            "subject", "comment"]
