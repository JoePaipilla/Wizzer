from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('follows/', views.follows, name='follows'),
    path('profile/<username>/', views.profile_page, name='profile-page'),
    path('notifications/', views.notifications, name='notifications'),
    path('directmessages/', views.direct_messages, name='directmessages'),
    path('gallery/', views.gallery, name='gallery'),
    path('settings/', views.settings, name='settings'),
    path('testing/', views.testing, name='testing')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
