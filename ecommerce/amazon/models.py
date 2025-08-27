from django.db import models

# Create your models here.

class student(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.CharField(max_length=30, default="0")
    password=models.CharField(max_length=10,default="0")
    def __str__(self):
        return self.fname
class calculator(models.Model):
    num1=models.CharField(max_length=10)
    num2 = models.CharField(max_length=10)
    op = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    def __str__(self):
        return self.op


class employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    photo = models.FileField(upload_to='media/photo',default='0')

    def __str__(self):
        return self.fname