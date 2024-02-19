from .forms import BookForm
from .filter import BookFilter
from django.shortcuts import render, redirect
from .serializers import BookSerializer
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required
def book_list(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        print("12312312")
        if form.is_valid():
            print("sadasdasd")
            form.save()
            return redirect('books')
        else:
            print(form.errors)

    form = BookForm()
    books = BookFilter(request.GET, queryset=Book.objects.all())
    filtered_books = books.qs
    serializer = BookSerializer(filtered_books, many=True, read_only=True)

    context = {
        'form': form,
        'filterForm': books.form,
        'qs': serializer.data,
    }
    return render(request, 'book_list.html', context)


def book_update(request, pk):
    obj = Book.objects.get(pk=pk)
    form = BookForm(instance=obj)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('books')
    template_name = 'update_url.html'
    context = {'form': form}
    return render(request, template_name, context)


def book_delete(request, pk):
    obj = Book.objects.get(pk=pk)  # uuid kullanılması daha dogru olur artan id yerine kitap sayfa 249
    if request.method == 'POST':
        obj.delete()
        return redirect('books')
    template_name = 'delete_url.html'
    context = {'obj': obj,
               'name': 'Book',
               }
    return render(request, template_name, context)


def book_detail(request, pk):
    qs = Book.objects.get(pk=pk)
    template_name = 'book-detail.html'
    context = {'qs': qs}
    return render(request, template_name, context)
