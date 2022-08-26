""" Service Views """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Service, Category
from .forms import ServiceForm


def all_services(request):
    """ View to show all services, including search queries"""
    services = Service.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            services = services.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.info(request, "No search criteria entered!\
                              We have listed all of our services.")
                return redirect(reverse('services'))

            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
            services = services.filter(queries)

    context = {
        'services': services,
        'search': query,
        'current_categories': categories,
    }

    return render(request, 'services/services.html', context)


@login_required
def service_detail(request, service_id):
    """ View to show individual services"""

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)


@login_required
def add_service(request):
    """Adding a new service to the site"""
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'New Service Added.')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Oopps!!! Something went wrong.\
                Please ensure the form is filled in correctly')
    else:
        form = ServiceForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_service(request, service_id):
    """ Edit a service """
    if request.user.is_superuser:
        service = get_object_or_404(Service, pk=service_id)
        if request.method == 'POST':
            form = ServiceForm(request.POST, request.FILES, instance=service)
            if form.is_valid():
                form.save()
                messages.success(request, 'Update Successful!')
                return redirect(reverse('service_detail', args=[service.id]))
            else:
                messages.error(request, 'Update Failed.\
                    Please ensure the form is valid.')
        else:
            form = ServiceForm(instance=service)
            messages.info(request, f'You are editing {service.name}')

        template = 'services/edit_service.html'
        context = {
            'form': form,
            'service': service,
        }

        return render(request, template, context)
    else:
        messages.error(request, "You don't have access to this feature")
        return redirect(reverse('home'))


@login_required
def delete_service(request, service_id):
    """ Delete a service """
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Service has been deleted')
    return redirect(reverse('services'))
