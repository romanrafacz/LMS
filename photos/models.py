from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.

class Photo(models.Model):
    serial = models.CharField(max_length=255)
    title = models.CharField('title', max_length=255)
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=250)
    file = models.FileField(upload_to="photos/")
    create = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Photo"

    def __unicode__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse("photo_detail", args=[str(self.slug)])

    def get_next(self):
        next = Photo.ojbects.filter(serial_gt=self.serial)
        if next:
            return next[0]
        return None

    def get_previous(self):
        prev = Photo.objects.filter(serial_lt=self.serial).order_by('serial')
        if prev:
            return prev[0]
        return None




