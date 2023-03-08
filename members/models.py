from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import os

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Welcome(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SubscribedUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    date_created = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.email
