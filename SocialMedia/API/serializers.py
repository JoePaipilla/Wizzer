from django.contrib.auth.models import User
from SocialMedia.models import WizzerUser, Whiz

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]


class WhizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Whiz
        fields = [
            'whiz_poster',
            'content',
            'time_posted',
            'likes',
            'dislikes'
        ]