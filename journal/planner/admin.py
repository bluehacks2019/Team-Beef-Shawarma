from django.contrib import admin
from .models import Day
from .models import Plans, Tips
# Register your models here.

admin.site.register(Day)
admin.site.register(Plans)
admin.site.register(Tips)

