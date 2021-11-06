from django.db import models

# Create your models here.

class User(models.Model):
    deviceId = models.CharField(max_length=20)
