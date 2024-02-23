from django.shortcuts import render, redirect
from books.models import Book
from django.contrib.auth.decorators import login_required
from .models import Cart
from django.contrib import messages


@login_required
def cart_add(request, book_id):
    cart_item = Cart.objects.filter(user=request.user.id, book=book_id)
    print(cart_item)
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to your cart.")
    else:
        Cart.objects.create(user=request.user.id, book=book_id)
        messages.success(request, "Item added to your cart.")

    context = {
        'qs': cart_item
    }
    print(context)

    return render(request, 'bootstrap_base.html',context)




@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Book.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
