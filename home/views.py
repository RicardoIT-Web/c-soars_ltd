from django.shortcuts import render
from services.models import Service, Category
from django.shortcuts import redirect


def index(request):
    """ View to render index page"""

    return render(request, 'home/index.html')
