""" webhook handlers from stripe """
import json
import time
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from services.models import Service
from useraccount.models import UserAccount
from .models import Order, OrderItem


class StripeWH_Handler:
    """To handle stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

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
        purchase_order_details = intent.purchase_order
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in purchase_order_details.address.items():
            if value == "":
                purchase_order_details.address[field] = None

        account = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            account = UserAccount.objects.get(user__username=username)
            if save_info:
                account.email = purchase_order_details.email
                account.contact_number = purchase_order_details.contact_number
                account.address1 = purchase_order_details.address1
                account.address2 = purchase_order_details.address2
                account.city = purchase_order_details.city
                account.post_code = purchase_order_details.postcode
                account.country = purchase_order_details.country
                account.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=purchase_order_details.name,
                    user_account=account,
                    email__iexact=purchase_order_details.email,
                    phone_number__iexact=purchase_order_details.phone,
                    address1__iexact=purchase_order_details.address.line1,
                    address2__iexact=purchase_order_details.address.line2,
                    postcode__iexact=purchase_order_details.address.post_code,
                    city__iexact=purchase_order_details.address.city,
                    county__iexact=purchase_order_details.address.state,
                    country__iexact=purchase_order_details.address.country,
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
                self._send_confirmation_email(order)
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: \
                        Verified order is in database', status=200)
            else:
                order = None
                try:
                    order = Order.objects.create(
                        name=purchase_order_details.name,
                        email=purchase_order_details.email,
                        contact_number=purchase_order_details.contact_number,
                        address1=purchase_order_details.address.line1,
                        address2=purchase_order_details.address.line2,
                        postcode=purchase_order_details.post_code,
                        city=purchase_order_details.city,
                        county=purchase_order_details.state,
                        country=purchase_order_details.country,
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
                        content=f'Webhook received: {event["type"]} | ERROR: \
                            {e}', status=500)
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: \
                    Created order in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """To handle payment intent failed from stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
