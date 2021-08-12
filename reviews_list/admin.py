from django.contrib import admin
from .models import Reviews_list

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'review',
        'rating',
        'date',
    )

admin.site.register(Reviews_list, ReviewAdmin)
