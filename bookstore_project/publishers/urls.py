# books/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.publisher_list, name='publishers'),
    path('update/<int:pk>', views.publisher_update, name='update_url_publisher'),
    path('delete/<int:pk>', views.publisher_delete, name='delete_url_publisher'),
    path('filter/<int:pk>', views.publisher_filter, name='filter_url_publisher'),

]
