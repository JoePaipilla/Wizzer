from django.urls import path

from .views import UserAPIView, WhizAPIView

app_name = 'SocialMediaAPI'

urlpatterns = [
    path('User/<username>', UserAPIView.as_view(), name='UserAPIView'),
    path('Whizzes/', WhizAPIView.as_view(), name='WhizAPIView')
]