# books/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='categories'),
    path('update/<int:pk>', views.category_update, name='update_url_category'),
    path('delete/<int:pk>', views.category_delete, name='delete_url_category'),
]