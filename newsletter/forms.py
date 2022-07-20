from django import forms
from .models import Subscriber, Newsletter


class SubscriberForm(forms.ModelForm):
    """Subscriber form"""
    class Meta:
        """Form data"""
        model = Subscriber
        fields = ['email', ]


class NewsletterForm(forms.ModelForm):
    """newsletter form"""
    class Meta:
        """Form data"""
        model = Newsletter
        fields = ['subject', 'message', ]
