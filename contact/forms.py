from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    '''
    The contact form which connects to the views and provides the User with
    the required fields to be displayed at frontend
    '''
    class Meta:
        '''
        Calss meta to define which model to pull data from
        '''
        model = Contact
        fields = ('name', 'email', 'contact_number', 'subject', 'comment', )
