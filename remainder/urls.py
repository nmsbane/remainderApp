from django.conf.urls import url

from .views import AppointmentCreateView, AppointementJsonView

urlpatterns = [

    url(r'^/new$', AppointmentCreateView.as_view(), name='new_appointment'),
    url(r'^/jsonnew$', AppointementJsonView.as_view(), name='new_appointment_json'),
]
