import email
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class roles(models.TextChoices): 
    admin = "ADMIN"
    professor = "PROFESSOR"
    student = "STUDENT"
    tutor = "TUTOR"


class Account(models.Model):
    key = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    email = models.EmailField(max_length=50, blank=True)
    phone_number = models.IntegerField(max_length=10, blank=True)
    role = models.CharField(max_length=10,choices=roles.choices)