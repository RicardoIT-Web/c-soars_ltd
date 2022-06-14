from django.contrib import admin
from .models import Service, Category


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'includes',
        'description',
        'price',
        'spotters',
        'total_price',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
