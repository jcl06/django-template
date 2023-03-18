from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    #is_approver = models.BooleanField(default=False)
    full_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.full_name