from django.db import models

# Create your models here.

class newCustomer(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    adress = models.TextField(max_length=100)