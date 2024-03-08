from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import BookForm
from .filter import BookFilter
from django.shortcuts import render, redirect, get_object_or_404
from .serializers import BookSerializer
from .models import Book
from django.contrib.auth.decorators import login_required


def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return render(request, 'book_list.html', {'books': serializer.data})


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            data['html_book_list'] = render_to_string('partial_book_list.html', {
                'books': serializer.data
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()
    return save_book_form(request, form, 'partial_book_create.html')


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)
    return save_book_form(request, form, 'partial_book_update.html')


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        data['html_book_list'] = render_to_string('partial_book_list.html', {
            'books': serializer.data
        })
    else:
        serializer = BookSerializer(book, many=True)
        context = {'book': serializer.data}
        data['html_form'] = render_to_string('partial_book_delete.html', context, request=request)
    return JsonResponse(data)
































#
# @login_required
# def book_list(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return render(request, 'book_list.html', {'books': serializer.data})
#
#
# def book_create(request):
#     data = dict()
#
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             data['form_is_valid'] = True
#             books = Book.objects.all()
#             serializer = BookSerializer(books)
#             data['html_book_list'] = render_to_string('partial_book_list.html', {
#                 'books': serializer.data
#             })
#         else:
#             data['form_is_valid'] = False
#     else:
#         form = BookForm()
#
#     context = {'form': form}
#     data['html_form'] = render_to_string('partial_book_create.html',
#                                          context,
#                                          request=request
#                                          )
#     return JsonResponse(data)
#
#
# def book_update(request, pk):
#     obj = Book.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES, instance=obj)
#         if form.is_valid():
#             form.save()
#             return redirect('books')
#     else:
#         form = BookForm(instance=obj)
#     template_name = 'update_url.html'
#     context = {'form': form,
#                'pk': pk,
#                }
#     return render(request, template_name, context)
#
#
# def book_delete(request, pk):
#     obj = Book.objects.get(pk=pk)  # uuid kullanılması daha dogru olur artan id yerine kitap sayfa 249
#     if request.method == 'POST':
#         obj.delete()
#         return redirect('books')
#     template_name = 'delete_url.html'
#     context = {'obj': obj,
#                'name': 'Book',
#                }
#     return render(request, template_name, context)
#
#
# def book_detail(request, pk):
#     qs = Book.objects.get(pk=pk)
#     serializer = BookSerializer(qs, read_only=True)
#     template_name = 'book-detail.html'
#     context = {'qs': serializer.data}
#     return render(request, template_name, context)
