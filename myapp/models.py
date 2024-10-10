from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
    USER=[
        ('admin','Admin'),
        ('teacher','Teacher'),
        ('student','Student')
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)

    def  __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}-{self.user_type}"
