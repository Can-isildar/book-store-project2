from django.contrib import admin
from .models import Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["fullname", "birth_date"]


admin.site.register(Author, AuthorAdmin)
