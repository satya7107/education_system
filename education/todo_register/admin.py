from django.contrib import admin

# Register your models here.

from .models import todoregisternew
class regadminall (admin.ModelAdmin):
    list_display=('username','email','rol_name','updated_at')
    search_fields=('username','email','rol_name')
admin.site.register(todoregisternew,regadminall)
