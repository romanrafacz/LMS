from django.contrib import admin

from lms.models import JMWClassInfo
# Register your models here.

@admin.register(JMWClassInfo)
class JMWClassAdmin(admin.ModelAdmin):
    list_display = ('jmw_name', 'avnet_type_name', 'start_date', 'end_date', 'duration', 'public', 'class_status',
                    'total_registered', 'instructor_name', 'tech', 'labs')