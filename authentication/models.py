from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

USERTYPE = [("Employee", "EMPLOYEE"), ("Employer", "EMPLOYER")]


class UserModel(AbstractUser):
    userCountry = models.CharField(max_length=20,null=True,blank=True)
    userAge = models.IntegerField(null=True,blank=True)
    userType = models.CharField(max_length=10,choices = USERTYPE,default = "Employee")