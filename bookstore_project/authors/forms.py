from django import forms
from .models import Author


class AuthForm(forms.ModelForm):
    author_name = forms.CharField(max_length=100, label="Name ")
    author_surname = forms.CharField(max_length=100, label="Surname")

    class Meta:
        model = Author
        fields = ("author_name", "author_surname", "birth_date")