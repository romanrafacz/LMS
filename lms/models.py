from django.db import models

import json

# Create your models here.

class AvnetTypeInfo(models.Model):
    avnet_type_id = models.IntegerField()
    avnet_name = models.CharField(null=True, max_length=50) 
    avnet_title = models.TextField(null=True)
    last_modified_str = models.CharField(null=True, max_length=25) 
    created_str = models.CharField(null=True, max_length=25) 
    last_modified = models.TimeField(null=True)
    last_modified_by= models.CharField(null=True, max_length=100) 
    created = models.TimeField(null=True)
    classroom_delivery_method = models.CharField(null=True, max_length=200) 

class AvnetDescription(models.Model):
    avnet_description_id = models.IntegerField() 
    avnet_type_id = models.ForeignKey('AvnetTypeInfo') 
    avnet_name = models.CharField(null=True, max_length=50) 
    language = models.CharField(null=True, max_length=10) 
    descrtiption = models.TextField(null=True)
    overview = models.TextField(null=True)
    abstract = models.TextField(null=True)
    prerequisits = models.TextField(null=True)
    topic = models.TextField(null=True)
    last_modified= models.CharField(null=True, max_length=50) 
    created = models.CharField(null=True, max_length=50)

class ClassPlSummary(models.Model):
    pl_summary_id = models.IntegerField()
    jmw_class_info_id = models.IntegerField(null=True)
    avent_type_info_id = models.IntegerField(null=True)
    jmw_name = models.CharField(null=True, max_length=50)
    avnet_name = models.CharField(null=True, max_length=50)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    jmw_locaiton_info_id = models.IntegerField(null=True)
    instructor_id = models.IntegerField(null=True)
    instructor_name = models.CharField(null=True, max_length=100)
    facility_expense = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    material_expense = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    lab_expense = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    travel_expense = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    instructor_expense = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    other_expense = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    total_expense = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    class_prce = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    total_attend = models.IntegerField(null=True)
    total_jmw_attend = models.IntegerField(null=True)
    gross_receipts = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    net_profit = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    gross_jmw_receipts = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    po = models.CharField(null=True, max_length=50)
    currency = models.CharField(null=True, max_length=50)
    instructor_rate = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    net_profit = models.DecimalField(null=True, max_digits=6, decimal_places=2)

class JMWClassInfo(models.Model):
    jmw_class_info_id = models.IntegerField()
    jmw_name = models.CharField(unique=True, null=True, max_length=25)
    avnet_type_info_id = models.IntegerField(null=True)
    avnet_type_name = models.CharField(null=True, max_length=50)
    start_date_str = models.CharField(null=True, max_length=50)
    end_date_str = models.CharField(null=True, max_length=50)
    last_modified_str = models.CharField(null=True, max_length=25)
    created_str = models.CharField(null=True, max_length=25)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.CharField(null=True, max_length=100)
    last_modified = models.CharField(null=True, max_length=100)
    last_modified_by = models.CharField(null=True, max_length=100)
    start_date_local = models.DateField(null=True)
    end_date_local = models.DateField(null=True)
    duration = models.IntegerField(null=True)
    duration_unit = models.CharField(null=True, max_length=10)
    public = models.CharField(null=True, max_length=10)
    class_status = models.CharField(null=True, max_length=10)
    gtr = models.CharField(null=True, max_length=10)
    total_registered = models.IntegerField(null=True)
    total_jmw_registered = models.IntegerField(null=True)
    instructor = models.IntegerField(null=True)
    instructor_name = models.CharField(null=True, max_length=100) 
    type_url = models.CharField(null=True, max_length=200) 
    title = models.TextField(null=True)
    category = models.CharField(null=True, max_length=200) 
    price = models.IntegerField(null=True)
    owned_by = models.CharField(null=True, max_length=100) 
    source_by = models.CharField(null=True, max_length=100) 
    currency = models.CharField(null=True, max_length=25) 
    jmw_locaiton_info_id = models.IntegerField(null=True)
    room_info_id = models.IntegerField(null=True)
    subcategory = models.CharField(null=True, max_length=200) 
    notes = models.TextField(null=True)
    po = models.CharField(null=True, max_length=50) 
    tech = models.CharField(null=True, max_length=50) 
    labs = models.CharField(null=True, max_length=50) 
    lock_price = models.CharField(null=True, max_length=1)

    class Meta:
        abstract = False

    def __unicode__(self):
        return "jmw_name: %s" % self.jmw_name


#class Report(models.Model):
#    jmw_name = models.ManyToManyField('JMWClassInfo', to_field='jmw_name')
#    name = models.CharField(max_length=255)
#    company = models.CharField(max_length=50)
#    email = models.CharField(max_length=100)
#    phone = models.CharField(max_length=25)


