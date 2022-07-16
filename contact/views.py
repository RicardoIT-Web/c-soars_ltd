""" Contact Us Views """
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm


def index(request):
    """ home page view """
    return render(request, "home/index.html")


def contact(request):
    """ a view to render contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = {'subject': form.cleaned_data['subject']}
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'contact_number': form.cleaned_data['contact_number'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())
            messages.success(request, "Thank you! Your Inquiry has been submitted.\
                             We'll revert back with a response as soon as\
                             possible")

            try:
                send_mail(subject, message, 'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header.')

    form = ContactForm()
    return render(request, 'contact.html', {'form': form})
