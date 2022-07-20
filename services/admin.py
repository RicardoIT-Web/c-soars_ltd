""" admin views for services app """
from django.contrib import admin
from .models import Service, Category


class ServiceAdmin(admin.ModelAdmin):
    """ Service Admin View """
    list_display = (
        'created_on',
        'user',
        'category',
        'name',
        'description',
        'includes',
        'images',
        'price',
        'spotters',
        'total_price',
        'comment',
        'status',
    )
    search_fields = ('name', 'description', 'includes', 'price', 'status')
    list_filter = ('name', 'description', 'price', 'status')
    summernote_fields = ('comment')


class CategoryAdmin(admin.ModelAdmin):
    """ Service Admin View """
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
