# books/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='books'),
    path('update/<int:pk>', views.book_update, name='update_url_book'),
    path('delete/<int:pk>', views.book_delete, name='delete_url_book'),
]
