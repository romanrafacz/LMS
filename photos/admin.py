from django.contrib import admin

from photos.models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    

# Register your models here.
#admin.site.register(Photo, PhotoAdmin)

