from django import forms
from .models import Publisher

class PublishForm(forms.ModelForm):
    publisher_name = forms.CharField(max_length=100)
    establish_year = forms.DateField()

    class Meta:
        model = Publisher
        fields = ("publisher_name", "establish_year")