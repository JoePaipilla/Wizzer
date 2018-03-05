from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('WizzerUserList/', views.WizzerUserList.as_view()),
    path('WhizList/', views.WhizList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)