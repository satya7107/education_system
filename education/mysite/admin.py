from django.contrib import admin

# Register your models here.
from .models import employee
admin.site.register(employee)

from .models import student
admin.site.register(student)

from .models import user
admin.site.register(user)

from .models import all_experties
admin.site.register(all_experties)

from .models import all_experties_ceo
admin.site.register(all_experties_ceo)

from .models import all_experties_chanc
admin.site.register(all_experties_chanc)

from .models import all_experties_prince
admin.site.register(all_experties_prince)

from .models import all_experties_vice
admin.site.register(all_experties_vice)

from .models import all_experties_fact
admin.site.register(all_experties_fact)


from .models import uregister
class regadmin(admin.ModelAdmin):
    list_display=('username','email')
admin.site.register(uregister,regadmin)



from .models import main_register
class mregadmin(admin.ModelAdmin):
    list_display=('username','email','rollname','contact')
admin.site.register(main_register,mregadmin)