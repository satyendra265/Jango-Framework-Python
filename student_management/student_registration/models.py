from django.db import models

# Create your models here.
class student(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.CharField(max_length=30, default="0")
    password=models.CharField(max_length=10,default="0")
    def __str__(self):
        return self.fname