from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserAccount
from .forms import UserAccountForm
from payment.models import Order


@login_required
def useraccount(request):
    """
    Display User account
    """
    useraccount = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=useraccount)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')

    form = UserAccountForm(instance=useraccount)
    orders = useraccount.orders.all()

    template = 'useraccount/useraccount.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def purchase_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'Purchase History for order number {order_number}.'
        f'A confirmation email would have been sent on {order.date}.'
    ))

    template = 'payment/payment_successful.html'
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)
