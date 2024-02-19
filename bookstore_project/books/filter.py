import django_filters
from django import forms
from django.db import models
from .models import Book, Author, Category, Publisher


class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(label='name', field_name='book_name', lookup_expr='icontains')
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all())
    publisher = django_filters.ModelChoiceFilter(queryset=Publisher.objects.all())
    price = django_filters.RangeFilter()
    categories = django_filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = {
            'book_name',
            'author',
            'publisher',
            'categories',
            'price',
            'ISBN',
        }

    filter_overrides = {
        models.CharField: {
            'filter_class': django_filters.CharFilter,
            'extra': lambda f: {
                'lookup_expr': 'icontains',
            },
        },
        models.DateTimeField: {
            'filter_class': django_filters.DateFilter,
            'extra': lambda f: {
                'widget': forms.DateInput(attrs={'type': 'date'}),
            },
        },
    }
