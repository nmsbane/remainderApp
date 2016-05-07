from celery import shared_task
from django.core.mail import send_mail
from .models import Appointement
from dateutil import tz

import arrow


@shared_task
def send_remainder_email(appointement_id):
    """Send a remainder using email"""
    try:
        appointment = Appointement.objects.get(id=appointement_id)
    except Appointement.DoesNotExist:
        return

    appointment_time = arrow.get(appointment.time).replace(tzinfo=tz.gettz(str(appointment.timezone)))
    print appointment_time
    subject = 'Hi You have an appointment coming up at {0}.'.format(
        appointment_time.format('h:mm a')
    )
    message = appointment.message
    send_mail(subject, message, 'admin@remainder.com', [appointment.email])


