from datetime import datetime

from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_surname = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)

    def fullname(self):
        return f"{self.author_name} {self.author_surname}"

    def __str__(self):
        return self.fullname()
