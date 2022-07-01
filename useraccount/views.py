from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserAccount
from .forms import UserAccountForm


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
