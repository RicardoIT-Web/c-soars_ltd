""" Briefcase tools """
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name='calc_subtotal2')
def calc_subtotal2(total_price, quantity):
    return total_price * quantity
