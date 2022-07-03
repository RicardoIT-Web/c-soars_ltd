from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from briefcase.content import briefcase_content
import stripe


def payment(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    briefcase = request.session.get('briefcase', {})
    if not briefcase:
        messages.error(request, "Your Briefcase is currently empty")
        return redirect(reverse('services'))

    current_purchase = briefcase_content(request)
    total = current_purchase['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )

    form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Missing Stripe Public Key')

    template = 'payment/payment.html'
    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
