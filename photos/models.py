from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField(unique=True)
    file = models.FileField(upload_to="photos/")

    class Meta:
        verbose_name = "Photo"

    def __unicode__(self):
        return "%s" % self.title

