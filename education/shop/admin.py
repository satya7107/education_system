from django.contrib import admin

# Register your models here.
from .models import products
class prodadmin(admin.ModelAdmin):
    list_display = ('product_name', 'price')
admin.site.register(products,prodadmin)

from .models import scontact
class contadmin(admin.ModelAdmin):
    list_display = ('name', 'email','desc')
admin.site.register(scontact,contadmin)