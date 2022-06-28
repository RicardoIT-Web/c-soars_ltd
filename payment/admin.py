"""
to view the full order in the admin view
"""
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInLine(admin.TabularInline):
    """
    Allows to add and edit line items in the admin
    from inside the order model
    """
    model = OrderItem
    readonly_fields = ('orderitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    to view the full order
    """
    inlines = (OrderItemAdminInLine,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'grand_total',)

    fields = ('order_number', 'name',
              'email', 'contact_number',
              'address1', 'address2',
              'post_code', 'city', 'county',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'name',
                    'order_total', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
