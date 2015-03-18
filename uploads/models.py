from django.db import models

# Create your models here.

class Part(models.Model):
    training_id = models.CharField(max_length=25)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
