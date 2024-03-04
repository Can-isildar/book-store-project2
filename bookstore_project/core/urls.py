# books/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.home, name='home'),
    path('editprofile/', views.edit_profile, name='edit_profile'),
]
