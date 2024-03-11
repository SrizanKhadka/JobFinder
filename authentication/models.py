from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

USERTYPE = [
    ("EMPLOYEE"),("Employee"),
    ("EMPLOYER"),("Employer")
]

class UserModel(AbstractUser):
    userCountry = models.CharField(default=None)
    userAge = models.IntegerField(default=None)
    userType = models.CharField(max_length=10,choices = USERTYPE,default = "Employee")