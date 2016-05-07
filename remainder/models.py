from django.db import models
from timezone_field import TimeZoneField
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
import arrow

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

    def clean(self):
        """Checks that appointments are not scheduled in the past"""

        appointment_time = arrow.get(self.time, self.timezone.zone)

        if appointment_time < arrow.utcnow():
            raise ValidationError('Cannot schedule an appointment for the past')

    def schedule_reminder(self):
        """Schedules a Celery task to send a reminder about this appointment"""

        # Calculate the correct time to send this reminder
        appointment_time = arrow.get(self.time, self.timezone.zone)

        # Avoid circular dependency
        from .tasks import send_remainder_email
        send_remainder_email.apply_async((self.pk,), eta=appointment_time)

    def save(self, *args, **kwargs):
        """Save method which schedules a reminder"""

        # we need self.pk, so save it first
        super(Appointement, self).save(*args, **kwargs)

        # Schedule a new reminder task for this appointment
        self.schedule_reminder()

        super(Appointement, self).save(*args, **kwargs)

