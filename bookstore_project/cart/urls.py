from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:pk>/', views.add_to_cart, name='cart_add'),
    path('del/<int:pk>/', views.remove_to_cart, name='remove_to_cart'),
    # path('cart_clear/', views.cart_clear, name='cart_clear'),
    # path('cart-detail/', views.cart_detail,name='cart_detail'),
]