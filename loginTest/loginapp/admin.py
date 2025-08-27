from django.contrib import admin
from .models import newUser
# Register your models here.
@admin.register(newUser)
class newUser(admin.ModelAdmin):
    list_display = ['id','First_name','Last_name']