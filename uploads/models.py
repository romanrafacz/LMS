from django.db import models

# Create your models here.

class Part(models.Model):
    jmw_name = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)

    class Meta:
        abstract = False

