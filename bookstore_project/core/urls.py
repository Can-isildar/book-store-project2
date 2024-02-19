# books/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('get-datail/', views.get_profile_detail, name="get-profile-detail"),
    path('homepage/', views.home, name='home'),
    path('editprofile/',views.edit_profile, name='edit_profile'),
]
