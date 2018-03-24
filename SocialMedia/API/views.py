from django.contrib.auth.models import User

from rest_framework import generics

from .serializers import UserSerializer, WhizSerializer
from SocialMedia.models import WizzerUser, Whiz


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'username'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class WhizAPIView(generics.ListCreateAPIView):
    serializer_class = WhizSerializer

    def get_queryset(self):
        return Whiz.objects.all()[::-1]
