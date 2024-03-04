from .models import Cart
from .serializers import CartSerializer


def cart_context_processor(request):
    cart_items = []
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart_items, many=True)
        cart_ordered_dicts = serializer.data
        cart_items = [dict(item) for item in cart_ordered_dicts]
    else:
        cart_items = []
    return {'cart': cart_items}


def cart_items_count(request):
    cart_items_count = 0  # Kullanıcı oturumu kapalıysa 0 olarak varsayalım
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).count()
    return {'cart_items_count': cart_items_count}


