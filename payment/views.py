from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def payment(request):
    briefcase = request.session.get('briefcase', {})
    if not briefcase:
        messages.error(request, "Your Briefcase is currently empty")
        return redirect(reverse('services'))

    form = OrderForm()
    template = 'payment/payment.html'
    context = {
        'form': form,
        'stripe_public_key': 'pk_test_51L2aidB28RWqcdkUOHQyzryg2UxBKx1F1cBowy4aPlXzqJ7phD1cx45YSx2lp0PObM9rsOwlbyznRCgilTsTFbkb006blWp7tb',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
