from django.shortcuts import render


def index(request):
    """ View to render home page"""

    return render(request, 'home/index.html')
