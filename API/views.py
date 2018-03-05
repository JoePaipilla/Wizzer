from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from SocialMedia.models import WizzerUser, Whiz

from .serializers import WizzerUserSerializer, WhizSerializer


class WizzerUserList(APIView):

    def get(self, request):
        wizzerusersall = WizzerUser.objects.all()
        serializer = WizzerUserSerializer(wizzerusersall, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class WhizList(APIView):

    def get(self, request):
        whizzes = Whiz.objects.all()
        serializer = WhizSerializer(whizzes, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass