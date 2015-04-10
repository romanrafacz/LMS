from django.contrib import admin
from uploads.models import Part

# Register your models here.
@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'phone')
