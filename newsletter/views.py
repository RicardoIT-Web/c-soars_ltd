"""newsletter views"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django_pandas.io import read_frame
from .forms import SubscriberForm, NewsletterForm
from .models import Subscriber


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


@login_required
def newsletter(request):
    """Form for sending newsletters"""
    emails = Subscriber.objects.all()
    dataframe = read_frame(emails, fieldnames=['email'])
    mail_list = dataframe['email'].values.tolist()
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            send_mail(
                subject,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Newsletter has been issued!')
            return redirect('newsletter')
    else:
        form = NewsletterForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter.html', context)
