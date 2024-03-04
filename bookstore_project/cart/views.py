from django.http import JsonResponse
from django.shortcuts import render, redirect
from books.models import Book
from django.contrib.auth.decorators import login_required
from .models import Cart


@login_required
def add_to_cart(request, pk):
    book = Book.objects.get(pk=pk)
    cart, created = Cart.objects.get_or_create(user_id=request.user.id, book=book)
    if not created:
        cart.quantity += 1
        cart.save()
    return redirect('books')

def remove_to_cart(request, pk):
    cart = Cart.objects.get(pk=pk)
    cart.delete()

    return redirect('books')


