""" Contact Us Views """
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm


def index(request):
    return render(request, "home/index.html")


def contact(request):
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

            try:
                send_mail(subject, message, 'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header.')
            return redirect('home')

    form = ContactForm()
    return render(request, 'contact.html', {'form': form})
