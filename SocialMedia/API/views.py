from django.contrib.auth.models import User

from rest_framework import generics

from .serializers import UserSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'username'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

