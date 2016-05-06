from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Appointement

# Create your views here.


class AppointmentCreateView(CreateView):
    """ Shows a form to crete a new appointment view"""
    model = Appointement
    fields = ['email', 'message', 'time', 'timezone']

