from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Appointement
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class AppointmentCreateView(SuccessMessageMixin, CreateView):
    """ Shows a form to crete a new appointment view"""
    model = Appointement
    fields = ['email', 'message', 'time', 'timezone']
    success_message = 'Appointment successfully created'

