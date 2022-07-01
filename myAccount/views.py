from django.shortcuts import render


def account(request):
    """
    View to display User account
    """
    template = "accounts/account.html"
    context = {}

    return render(request, template, context)
