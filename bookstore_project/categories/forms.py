from django import forms
from .models import Category


class CatForm(forms.ModelForm):
    name = forms.CharField(max_length=100)

    class Meta:
        model = Category
        fields = ("name",)


