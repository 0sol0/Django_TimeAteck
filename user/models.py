from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = 'User'
        
    phone = models.CharField(max_length=24)
    address = models.CharField(max_length=256)