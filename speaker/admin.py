from django.contrib import admin

from speaker.models import SpeakerInfo

# Register your models here.

@admin.register(SpeakerInfo)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'mobile_phone', 'city', 'state')
