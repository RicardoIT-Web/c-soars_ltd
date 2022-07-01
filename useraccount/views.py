from django.shortcuts import render, get_object_or_404
from .models import UserAccount


def useraccount(request):
    """
    Display User account
    """
    accounts = get_object_or_404(UserAccount, user=request.user)

    template = 'useraccount/useraccount.html'
    context = {
        'accounts': accounts,
    }

    return render(request, template, context)
