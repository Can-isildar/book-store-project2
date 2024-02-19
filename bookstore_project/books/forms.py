from django import forms
from .models import Author, Publisher, Category, Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    book_name = forms.CharField(required=False)

    price = forms.FloatField(required=True, min_value=0)

    ISBN = forms.CharField(max_length=20)

    author = forms.ChoiceField(required=False,
                               choices=[(author.id, author.fullname()) for author in Author.objects.all()])
    publisher = forms.ChoiceField(required=False, choices=[(publisher.id, publisher.publisher_name) for publisher in
                                                           Publisher.objects.all()])
    categories = forms.ChoiceField(required=False,
                                   choices=[(category.id, category.name) for category in Category.objects.all()])
    pub_time = forms.DateField()

    class Meta:
        model = Book
        fields = ("book_name", "price", "author", "publisher", "categories", "pub_time", "ISBN")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].choices = [(None, '---------')] + [(author.id, author.fullname()) for author in
                                                                 Author.objects.all()]
        self.fields['book_name'].choices = [(None, '---------')] + [(book.dbid, book.book_name) for book in
                                                                    Book.objects.all()]

        self.fields['publisher'].choices = [(None, '---------')] + [(publisher.id, publisher.publisher_name) for
                                                                    publisher in Publisher.objects.all()]

        self.fields['categories'].choices = [(None, '---------')] + [(category.id, category.name) for category in
                                                                     Category.objects.all()]