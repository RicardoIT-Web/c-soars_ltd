from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from services.models import Service


def view_briefcase(request):
    """ View to render briefcase page to show services booked"""

    return render(request, 'briefcase/briefcase.html')


def add_to_briefcase(request, item_id):
    """ add qty of specified service to briefcase """

    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    briefcase = request.session.get('briefcase', {})

    if item_id in list(briefcase.keys()):
        briefcase[item_id] += quantity
        messages.success(request, f'Updated {service.description} to quantity of {briefcase[item_id]}')
    else:
        briefcase[item_id] = quantity
        messages.success(request,
                         f'{service.description} added to your briefcase')

    request.session['briefcase'] = briefcase
    return redirect(redirect_url)


def adjust_briefcase(request, item_id):
    """ adjust qty of specified service to briefcase """

    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    briefcase = request.session.get('briefcase', {})

    if quantity > 0:
        briefcase[item_id] = quantity
        messages.success(request, f'Updated {service.description}  to quantity of {briefcase[item_id]}')
    else:
        briefcase.pop(item_id)
        messages.success(request, f'{service.description} removed from your briefcase')

    request.session['briefcase'] = briefcase
    return redirect(reverse('view_briefcase'))


def remove_from_briefcase(request, item_id):
    """ remove item of specified service from briefcase """

    try:
        service = get_object_or_404(Service, pk=item_id)
        briefcase = request.session.get('briefcase', {})
        briefcase.pop(item_id)
        messages.success(request, f'{service.description} removed from your briefcase')

        request.session['briefcase'] = briefcase
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing service: {e}')
        return HttpResponse(status=500)
