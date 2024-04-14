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



from .models import sorder
class orderadmin(admin.ModelAdmin):
    list_display=('order_id','name','state')
admin.site.register(sorder,orderadmin)



from .models import order_update
class order_update_admin(admin.ModelAdmin):
    list_display=('order_id', 'update_desc','timestamp')
admin.site.register(order_update,order_update_admin)