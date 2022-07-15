""" Views for User Account features """
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from payment.models import Order
from services.models import Service
from .models import UserAccount, ReviewRating
from .forms import UserAccountForm, ReviewRatingForm


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
            messages.error(request, 'Update failed. Please ensure the form\
                           is valid.')
    else:
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
    """ View to display purchase history """
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


def submit_review(request, service_id):
    """ View to display User review form """
    service = get_object_or_404(Service, pk=service_id)

    if request.method == 'POST':
        form = ReviewRatingForm(request.POST)
        if form.is_valid():
            review_form = form.save(commit=False)
            review_form.service = service
            review_form.user = request.user
            form.save()
            messages.success(request, 'Review submitted successfully!')
        else:
            messages.error(request, 'Failed to submit review. Please ensure\
                           the form is valid.')
    else:
        form = ReviewRatingForm()

    template = 'useraccount/submit_review.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


class Reviews(ListView):
    """ A view to render reviews """
    model = ReviewRating
    template_name = 'useraccount/reviews.html'
