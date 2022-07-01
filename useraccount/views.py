from django.shortcuts import render


def useraccount(request):
    """
    Display User account
    """
    template = 'useraccount/useraccount.html'
    context = {}

    return render(request, template, context)
