""" Contact Us Views """
from django.shortcuts import render
from django.views import View
from .forms import ContactForm


class ContactFormView(View):
    '''
    This form is to display the contacts form in the frontend
    for the User to be able to view it
    '''

    def get(self, request):
        '''
        This gets the required data from the contactform
        '''
        context = {
            'contact_form': ContactForm()
        }
        return render(request, 'contact/contact.html', context)

    def post(self, request):
        '''
        This posts the User data from the frontend
        and sends that data to the backend
        '''
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()

        return render(request, 'contact/contact.html',)
