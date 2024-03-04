# Generated by Django 4.2.10 on 2024-02-29 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_img'),
        ('cart', '0007_alter_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='book',
        ),
        migrations.AddField(
            model_name='cart',
            name='book',
            field=models.ManyToManyField(null=True, to='books.book'),
        ),
    ]