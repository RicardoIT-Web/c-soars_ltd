""" Contact Us forms """
from django import forms


class ContactForm(forms.Form):
    '''
    The contact form which connects to the views and provides the User with
    the required fields to be displayed at frontend
    '''
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    contact_number = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
