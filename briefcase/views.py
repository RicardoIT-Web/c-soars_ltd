from django.shortcuts import render


def view_briefcase(request):
    """ View to render briefcase page to show services booked"""

    return render(request, 'briefcase/briefcase.html')