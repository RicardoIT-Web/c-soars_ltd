from django.shortcuts import render
from .forms import ContactForm
from django.views import View


def contact(request):
    return render(request, 'contact.html')
