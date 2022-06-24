"""Admin view of user reviews """
from django.contrib import admin
from .models import ReviewCard


class ReviewCardAdmin(admin.ModelAdmin):
    """Admin view of user reviews """
    list_display = ('user',
                    'service',
                    'comment',
                    'rating',
                    'created_on',
                    'updated_on',
                    'status')

    search_fields = ('user', 'service',
                     'rating', 'created_on',
                     'updated_on', 'status')

    ordering = ('-created_on')


admin.site.register(ReviewCard)
