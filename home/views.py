from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    """ View to render index page"""

    return render(request, 'home/index.html')
