from django.contrib import admin
from .models import newCustomer
# Register your models here.

#admin.site.register(newCustomer)
@admin.register(newCustomer)
class newCustomer(admin.ModelAdmin):
    list_display = ['id','firstname','lastname']