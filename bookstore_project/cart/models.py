from django.db import models
from books.models import Book
from django.contrib.auth.models import User

class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.quantity}  {self.book} {self.user} {self.date_added}'
