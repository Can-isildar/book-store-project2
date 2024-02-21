from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Category
from .forms import CatForm
from .serializers import CategorySerializer
from books.models import Book
from books.serializers import BookSerializer
from books.filter import BookFilter

@login_required
def category_list(request):
    form = CatForm()
    qs = Category.objects.all()
    serializer = CategorySerializer(qs, many=True)
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    template_name = 'category_list.html'
    context = {'form': form,
               'qs': serializer.data,
               }
    return render(request, template_name, context)


def category_update(request, pk):
    obj = Category.objects.get(pk=pk)
    form = CatForm(instance=obj)
    if request.method == 'POST':
        form = CatForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('categories')
    template_name = 'update_url.html'
    context = {'form': form,
               'name': 'Category',
               }
    return render(request, template_name, context)


def category_delete(request, pk):
    obj = Category.objects.get(pk=pk)  # uuid kullanılması daha dogru olur artan id yerine kitap sayfa 249
    if request.method == 'POST':
        obj.delete()
        return redirect('categories')
    template_name = 'delete_url.html'
    context = {'obj': obj,
               'name': 'Category',
               }
    return render(request, template_name, context)


def category_filter(request, pk):
    category = Category.objects.get(pk=pk)
    books = Book.objects.filter(categories=category)
    serializer = BookSerializer(books, many=True)
    filter_books = BookFilter(request.GET, queryset=Book.objects.all())
    context = {
        'qs': serializer.data
    }
    return render(request, 'book_list.html', context)