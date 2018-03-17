from django.urls import path

from .views import UserAPIView

app_name = 'SocialMediaAPI'

urlpatterns = [
    path('User/<username>', UserAPIView.as_view(), name='UserAPIView')
]