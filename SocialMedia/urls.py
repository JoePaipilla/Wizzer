from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('follows/', views.FollowsView.as_view(), name='follows'),
    path('profile/<username>/', views.profile_page, name='profile-page'),
    path('notifications/', views.NotificationsView.as_view(), name='notifications'),
    path('directmessages/', views.DirectMessagesView.as_view(), name='directmessages'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('settings/', views.SettingsView.as_view(), name='settings')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
