from django.contrib.auth.models import User
from SocialMedia.models import WizzerUser, Whiz

from rest_framework import serializers


class WhizSerializer(serializers.Serializer):

    whiz_poster = serializers.StringRelatedField()
    content = serializers.CharField()
    time_posted = serializers.DateTimeField()
    likes = serializers.StringRelatedField(many=True)
    dislikes = serializers.StringRelatedField(many=True)


class ProfileSerializer(serializers.Serializer):

    following = serializers.StringRelatedField(many=True)
    followers = serializers.StringRelatedField(many=True)
    gender = serializers.ChoiceField(choices='GENDER_CHOICES')
    whizzes = WhizSerializer(source='whiz_set', many=True)


class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    profile = ProfileSerializer(source='wizzeruser')