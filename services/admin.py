from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Service, Category


class ServiceAdmin(admin.ModelAdmin):
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
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
