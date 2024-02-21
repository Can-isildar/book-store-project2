from django.urls import path
from . import views


urlpatterns = [
    path('', views.author_list, name='authors'),
    path('update/<int:pk>', views.author_update, name='update_url_author'),
    path('delete/<int:pk>', views.author_delete, name='delete_url_author'),
    path('filter/<int:pk>', views.author_filter, name='filter_url_author')
]