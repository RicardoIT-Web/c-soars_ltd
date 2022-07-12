""" Signals for order management """
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    update order total when updating or creating a line item.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    update order total on each line item when deleted.
    """
    instance.order.update_total()
