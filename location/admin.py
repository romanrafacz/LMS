from django.contrib import admin

from location.models import JMWLocationInfo

# Register your models here.

@admin.register(JMWLocationInfo)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('description', 'street', 'city', 'state', 'postal_code', 'phone')
