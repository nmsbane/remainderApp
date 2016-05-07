from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Appointement
from django.contrib.messages.views import SuccessMessageMixin

from .serializers import AppointementSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AppointmentCreateView(SuccessMessageMixin, CreateView):
    """ Shows a form to crete a new appointment view"""
    model = Appointement
    fields = ['email', 'message', 'time', 'timezone']
    success_message = 'Appointment successfully created'


class AppointementJsonView(APIView):
    def post(self, request):
        serializer = AppointementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


