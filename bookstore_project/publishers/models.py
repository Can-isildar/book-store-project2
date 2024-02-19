from django.db import models


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=100)
    establish_year = models.DateField()

    def __str__(self):
        return self.publisher_name
