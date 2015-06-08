from django.db import models
from geoposition.fields import GeopositionField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.


class HospitalDirection(models.Model):
    name = models.CharField(max_length=50)
    formatted_address = models.CharField(max_length=50)
    direction = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '{}'.format(self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('hospital-list', (),
                {
                    'slug': self.slug,
        })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(HospitalDirection, self).save(*args, **kwargs)


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()


class Comment(models.Model):
    hospital = models.ForeignKey(
        HospitalDirection, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return '{}'.format(self.hospital)
