from django.contrib import admin
from .models import Publisher

class PublisherAdmin(admin.ModelAdmin):
    list_display = ["publisher_name", "establish_year"]


admin.site.register(Publisher, PublisherAdmin)

