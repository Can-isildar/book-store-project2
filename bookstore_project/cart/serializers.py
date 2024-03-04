from .models import Cart
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    book = serializers.StringRelatedField(many=False)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'book', 'date_added', 'quantity']
