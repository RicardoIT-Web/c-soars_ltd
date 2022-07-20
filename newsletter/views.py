from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm, NewsletterForm
from django.core.mail import send_mail


def subscribe(request):
    """subscribe to newsletter view"""
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('home')
    else:
        form = SubscriberForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/subscribe.html', context)


def newsletter(request):
    """Form for sending newsletters"""
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Newsletter has been issued!')
            return redirect('newsletter')
    else:
        form = NewsletterForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter.html', context)
