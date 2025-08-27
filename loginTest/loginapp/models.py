from django.db import models

# Create your models here.

class newUser(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Email = models.CharField(max_length=100)
    User_Name = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)