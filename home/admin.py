from django.contrib import admin
from .models import Product_item

# Register your models here.


class Product_itemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'qty',
    )


admin.site.register(Product_item, Product_itemAdmin)

