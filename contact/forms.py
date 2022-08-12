""" Contact Us forms """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    The contact form which connects to the views and provides the User with
    the required fields to be displayed at frontend
    """

    class Meta:
        """contact form content"""

        model = Contact
        fields = (
            "name",
            "email",
            "contact_number",
            "subject",
            "comment",
        )

    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    contact_number = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=250)
    comment = forms.CharField(widget=forms.Textarea, max_length=2000)
