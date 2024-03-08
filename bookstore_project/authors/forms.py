from django import forms
from .models import Author


class AuthForm(forms.ModelForm):
    author_name = forms.CharField(max_length=100, label="Name ")
    author_surname = forms.CharField(max_length=100, label="Surname")
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Author
        fields = ("author_name", "author_surname", "birth_date")