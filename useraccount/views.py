from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserAccount
from .forms import UserAccountForm
from payment.models import Order


def useraccount(request):
    """
    Display User account
    """
    accounts = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=accounts)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated')

    form = UserAccountForm(instance=accounts)
    orders = accounts.user_purchases.all()

    template = 'useraccount/useraccount.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def purchase_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'Purchase History for order number {order_number}.'
        'An email confirmation would have been sent on {self.order.date}'
    ))

    template = 'payment/payment_successful.html'
    context = {
        'oder': order,
        'from_profile': True
    }

    return render(request, template, context)
