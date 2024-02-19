from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ["book_name", "pub_time", "price"]


admin.site.register(Book, BookAdmin)
