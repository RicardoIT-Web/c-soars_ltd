""" Contact Admin views """
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''
    The contact feature for the admin view
    '''
    list_display = ('name', 'email', 'contact_number', 'comment', 'actioned')
    search_fields = ('name', 'email', 'number', 'actioned')
