from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Service


def all_services(request):
    """ View to show all services, including search queries"""

    services = Service.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered!")
                return redirect(reverse('services'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)

    context = {
        'services': services,
        'search': query,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """ View to show individual services"""

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)
