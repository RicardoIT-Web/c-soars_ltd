""" Contact Us forms """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = True

    class Meta:
        """contact form content"""

        model = Contact
        fields = ('name', 'email', 'contact_number', 'subject', 'comment',
                  'actioned')
