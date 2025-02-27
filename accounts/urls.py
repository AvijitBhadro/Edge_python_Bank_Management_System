from django.urls import path
from . views import UserRegistrationsView
urlpatterns = [
  
    path('', UserRegistrationsView.as_view(),name='register'),
]
