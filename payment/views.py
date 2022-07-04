import json
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import stripe
from services.models import Service
from briefcase.content import briefcase_content
from .forms import OrderForm
from .models import OrderItem, Order


@require_POST
def cache_payment_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'briefcase': json.dumps(request.session.get('briefcase',{})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, Your payment was not processed. \
            Please try again later.')
        return HttpResponse(content=e, status=400)


def payment(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        briefcase = request.session.get('briefcase', {})

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'contact_number': request.POST['contact_number'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'post_code': request.POST['post_code'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }
        form = OrderForm(form_data)
        if form.is_valid():
            order = form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_briefcase = json.dumps(briefcase)
            order.save()
            for item_id, item_data in briefcase.items():
                try:
                    service = Service.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            service=service,
                            quantity=item_data,
                        )
                        order_item.save()
                except Service.DoesNotExist:
                    messages.error(request, (
                        'Please contact us for assistance with your order')
                    )
                    order.delete()
                    return redirect(reverse('view_briefcase'))
            
            request.session['save_order'] = 'save_order' in request.POST
            return redirect(reverse('payment_successful', args=[order.order_number]))
        else:
            messages.error(request, 'Sorry, Something went wrong with your form.\
                Please check your form details.')
    else:
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


def payment_successful(request, order_number):
    """
    A view to handle a successful order.
    """
    save_order = request.session.get('save_order')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Purchase Order received. Thank you!\
        Your order number is {order_number}.\
        A confirmation email will be sent out to {order.email}.')

    if 'briefcase' in request.session:
        del request.session['briefcase']

    template = 'payment/payment_successful.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
