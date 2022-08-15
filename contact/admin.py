""" Contact Admin views """
from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    The contact feature for the admin view
    """

    list_display = ("name", "email", "contact_number", "subject", "comment",
                    "actioned")
    search_fields = ("name", "email", "contact_number", "actioned")


admin.site.register(Contact, ContactAdmin)
