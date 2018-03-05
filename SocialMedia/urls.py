from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('API/WizzerUserList/', views.WizzerUserList.as_view()),
    path('API/WhizList/', views.WhizList.as_view())
]

#temporary
urlpatterns = format_suffix_patterns(urlpatterns)