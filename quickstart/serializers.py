from django.contrib.auth.models import User
from rest_framework import serializers

from . import tasks


class UserSerializer(serializers.HyperlinkedModelSerializer):
    extra_info = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'extra_info']

    def get_extra_info(self, obj):
        return obj.username + obj.email

    def send_email_greeting(self):
        tasks.send_email_task.delay(self.data.get('username'), self.data.get('email'))

