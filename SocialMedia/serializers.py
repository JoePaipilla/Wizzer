from rest_framework import serializers
from .models import WizzerUser, Whiz


class WizzerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WizzerUser
        fields = '__all__'


class WhizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whiz
        fields = '__all__'
