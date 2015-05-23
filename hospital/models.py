from django.db import models

# Create your models here.
class HospitalDirection(models.Model):
    name = models.CharField(max_length=50)
    formatted_address = models.CharField(max_length=50)
    direction = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)