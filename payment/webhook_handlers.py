from django.http import HttpResponse
from .models import Order, OrderItem
from services.models import Service

import json
import time


class StripeWH_Handler:
    """To handle stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """To handle an unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """To handle payment intent succeeded from stripe"""
        intent = event.data.object
        pid = intent.id
        briefcase = intent.matadata.briefcase
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    address1__iexact=billing_details.address.line1,
                    address2__iexact=billing_details.address.line2,
                    postcode__iexact=billing_details.address.post_code,
                    city__iexact=billing_details.address.city,
                    county__iexact=billing_details.address.state,
                    country__iexact=billing_details.address.country,
                    grand_total=grand_total,
                    original_briefcase=briefcase,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
            if order_exists:
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order is in database',
                    status=200)
            else:
                order = None
                try:
                    order = Order.objects.create(
                        name=billing_details.name,
                        email=billing_details.email,
                        contact_number=billing_details.contact_number,
                        address1=billing_details.address.line1,
                        address2=billing_details.address.line2,
                        postcode=billing_details.post_code,
                        city=billing_details.city,
                        county=billing_details.state,
                        country=billing_details.country,
                        original_briefcase=briefcase,
                        stripe_pid=pid,
                    )
                    for item_id, item_data in json.loads(briefcase).items():
                        service = Service.objects.get(id=item_id)
                        if isinstance(item_data, int):
                            order_item = OrderItem(
                                order=order,
                                service=service,
                                quantity=item_data,
                            )
                            order_item.save()
                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500)
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
                    status=200)

    def handle_payment_intent_payment_failed(self, event):
        """To handle payment intent failed from stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
