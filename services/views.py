from django.shortcuts import render
from .models import Service


def all_services(request):
    """ View to show all services, including search queries"""

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)
