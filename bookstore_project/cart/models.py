from django.db import models
from books.models import Book
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(null=True, default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f' {self.book} : {self.user} : {self.date_added} : {self.quantity}'

    @property
    def total_price(self):
        cartitems = self.book
        total = sum([item.price for item in cartitems])
        return total

    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity
