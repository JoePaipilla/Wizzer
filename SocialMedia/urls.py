from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.login, {'template_name': 'SocialMedia/login.html'}, name='login'),
    path('register/', views.register, name='register')
]