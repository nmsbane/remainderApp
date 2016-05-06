from django.db import models
from timezone_field import TimeZoneField

# Create your models here.


class Appointement(models.Model):
    email = models.EmailField()
    message = models.TextField()
    time = models.DateTimeField()
    timezone = TimeZoneField(default='Asia/Kolkata')

    def __unicode__(self):
        return "Remainder #{0} - {1}".format(self.pk, self.message)

    