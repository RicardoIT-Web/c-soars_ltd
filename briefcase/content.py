from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Service


def briefcase_content(request):

    briefcase_items = []
    total = 0
    service_count = 0
    briefcase = request.session.get('briefcase', {})

    for item_id, quantity in briefcase.items():
        service = get_object_or_404(Service, pk=item_id)
        total += quantity * (service.price + service.spotters)
        service_count += quantity
        briefcase_items.append({
            'item_id': item_id,
            'service': service,
            'service_desc': service.description,
            'quantity': quantity,
            'price': service.price,
        })

    grand_total = total

    context = {
        'briefcase_items': briefcase_items,
        'service_count': service_count,
        'total': total,
        'grand_total': grand_total,
    }

    return context
