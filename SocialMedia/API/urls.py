from django.urls import path, re_path

from .views import UserAPIView, WhizAPIView

app_name = 'SocialMediaAPI'

urlpatterns = [
    re_path('((?i)User/<username>)/$', UserAPIView.as_view(), name='UserAPIView'),
    re_path('((?i)AllWhizzes)/$', WhizAPIView.as_view(), name='WhizAPIView')
]