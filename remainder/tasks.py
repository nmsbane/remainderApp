from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import Appointement


import arrow


@shared_task
def send_email(appointement_id):
    """Send a remainder using email"""
    try:
        appointment = Appointement.objects.get(id=appointement_id)
    except Appointement.DoesNotExist:
        return

    appointment_time = arrow.get(appointment.time, appointment.time_zone.zone)
    subject = 'Hi You have an appointment coming up at {1}.'.format(
        appointment_time.format('h:mm a')
    )
    message = appointment.message
    send_mail(subject, message, 'admin@myblog.com', [appointment.email])
    

