from django.contrib import admin

# Register your models here.
from .models import products
class prodadmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'desc')
admin.site.register(products,prodadmin)