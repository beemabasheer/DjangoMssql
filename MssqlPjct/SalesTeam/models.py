from django.db import models

# Create your models here.

class SalesTeam(models.Model):
    first_name = models.CharField(max_length=500,blank=True)
    last_name = models.CharField(max_length=500,blank=True)
    email = models.CharField(max_length=500,blank=True)
    phone = models.CharField(max_length=500,blank=True)
    company = models.CharField(max_length=500,blank=True)
    hear_about_us = models.CharField(max_length=500,blank=True)
    comment = models.TextField()

