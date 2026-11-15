from django.contrib import admin
from unfold.admin import ModelAdmin

from myapp.models import Product

admin.site.site_title="Gen Shop"
admin.site.site_header="General Shop"
admin.site.index_title="Gen Shop"

# Register your models here.

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'cost', 'price', 'category', 'for_sale', 'discount')
    search_fields = ('name', 'code','category')
    list_filter = ('name', 'code', 'category')
    ordering = ('name','price')
    pass