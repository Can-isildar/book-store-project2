from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)
    publisher = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ('book_name', 'uuid', 'slug', 'price', 'pub_time', 'categories', 'publisher', 'author', 'dbid', 'ISBN')
