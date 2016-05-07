from django.db import models
from timezone_field import TimeZoneField
from django.core.urlresolvers import reverse

# Create your models here.


class Appointement(models.Model):
    email = models.EmailField()
    message = models.TextField()
    time = models.DateTimeField()
    timezone = TimeZoneField(default='Asia/Kolkata')

    def __unicode__(self):
        return "Remainder #{0} - {1}".format(self.pk, self.message)

    def get_absolute_url(self):
        return reverse('new_appointment')
