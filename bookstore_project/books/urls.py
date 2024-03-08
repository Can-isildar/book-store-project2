# books/urls.py


from django.urls import path, include
from . import views

app_name = "book"

urlpatterns = [
    path('', views.book_list, name='books'),
    path('create/', views.book_create, name='book_create'),
]

# urlpatterns = [
#     path('', views.book_list, name='books'),
#     path('update/<int:pk>', views.book_update, name='update_url_book'),
#     path('delete/<int:pk>', views.book_delete, name='delete_url_book'),
#     path('book-detail/<int:pk>', views.book_detail, name='book-detail'),
# ]
