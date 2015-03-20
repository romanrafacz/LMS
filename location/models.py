from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class JMWLocationInfo(models.Model):
    jmw_location_info_id = models.IntegerField()
    owner_code = models.CharField(max_length=25) 
    owner_id = models.IntegerField()
    location_code = models.CharField(max_length=200) 
    description = models.CharField(max_length=200) 
    street = models.CharField(max_length=100) 
    suite = models.CharField(max_length=50) 
    city = models.CharField(max_length=50) 
    state = models.CharField(max_length=20) 
    postal_code = models.CharField(max_length=25) 
    country = models.CharField(max_length=50) 
    web_page = models.CharField(max_length=50) 
    number_of_rooms = models.IntegerField()
    timezone = models.CharField(max_length=25) 
    default_type = models.CharField(max_length=10) 
    default_tech = models.CharField(max_length=25) 
    phone = models.CharField(max_length=25) 
    admin_name = models.CharField(max_length=100) 
    admin_email = models.CharField(max_length=50) 
    admin_phone= models.CharField(max_length=25) 
    tech_name = models.CharField(max_length=100) 
    tech_email = models.CharField(max_length=50) 
    tech_phone= models.CharField(max_length=25) 
    notes = models.TextField() 

class RoomInfo(models.Model):
    room_info_id = models.IntegerField()
    location_info_id = models.ForeignKey('JMWLocationInfo')
    room_name= models.CharField(max_length=50) 
    number_seats= models.IntegerField()
    cpu = models.CharField(max_length=50) 
    ram = models.CharField(max_length=25) 
    memory= models.CharField(max_length=25) 
    in_speed = models.CharField(max_length=25) 
