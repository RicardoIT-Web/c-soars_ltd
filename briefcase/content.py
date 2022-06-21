from django.conf import settings


def briefcase_content(request):

    briefcase_items = []
    total = 0
    service_count = 0

    contract = total

    context = {
        'briefcase_items': briefcase_items,
        'total': total,
        'service_count': service_count
    }

    return context
