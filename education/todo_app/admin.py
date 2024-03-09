from django.contrib import admin

# Register your models here.
from .models import todo_details
class todoadmin(admin.ModelAdmin):
    list_display=('task','is_complete','update_at')
    search_fields=('task','is_complete','update_at')

admin.site.register(todo_details,todoadmin)