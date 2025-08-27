from django.contrib import admin
from .models import student,employee
from .models import calculator
# Register your models here.

# admin.site.register(student)
admin.site.register(calculator)

@admin.register(student)
class student(admin.ModelAdmin):
    list_display = ['id','fname','lname']


@admin.register(employee)
class employee(admin.ModelAdmin):
    list_display = ['id','fname','lname']