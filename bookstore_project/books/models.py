from django.db import models
from authors.models import Author
from publishers.models import Publisher
from categories.models import Category
import uuid as uuid_lib
from django.utils.text import slugify


class Book(models.Model):
    dbid = models.AutoField(primary_key=True)
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    book_name = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=50, default="")
    pub_time = models.DateField()
    price = models.FloatField()
    categories = models.ManyToManyField(Category, related_name='books')
    author = models.ManyToManyField(Author, related_name='books', blank=True)
    publisher = models.ManyToManyField(Publisher, related_name='books', blank=True)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True,)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.book_name}-{self.dbid}")
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.book_name}-{self.dbid}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.book_name
