from .models import Appointement

from rest_framework import serializers
from django.utils import six


class AppointementSerializer(serializers.ModelSerializer):
    timezone = serializers.SerializerMethodField()

    class Meta:
        model = Appointement
        fields = ('email', 'message', 'time', 'timezone')

    def get_timezone(self, obj):
        return six.text_type(obj.timezone)
