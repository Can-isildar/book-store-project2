from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .forms import AuthForm
from .models import Author
from .serializers import AuthorSerializer
from books.models import Book
from books.serializers import BookSerializer
from books.filter import BookFilter
from django_ajax.decorators import ajax


@csrf_exempt
@login_required
def author_list(request):
    form = AuthForm()
    qs = Author.objects.all()
    serializer = AuthorSerializer(qs, many=True)

    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            author = form.save()
            serializer = AuthorSerializer(author)
            return JsonResponse({
                'success': True,
                'message': "Veri Başarıyla Eklendi",
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    template_name = 'author_list.html'
    context = {'form': form,
               'qs': serializer.data,
               }
    return render(request, template_name, context)


# def author_update(request, pk):
#     obj = Author.objects.get(pk=pk)
#     form = AuthForm(instance=obj)
#     if request.method == 'POST':
#         form = AuthForm(request.POST, instance=obj)
#         if form.is_valid():
#             form.save()
#     context = {'form': form, 'name': 'Author', 'obj': obj}
#     return JsonResponse(context)
@csrf_exempt
def author_update(request, pk):
    if request.method == 'POST':
        try:
            obj = Author.objects.get(pk=pk)
            form = AuthForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Author updated successfully'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)
        except (ValueError, KeyError):
            return JsonResponse({'message': 'Invalid request data'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def author_delete(request, pk):
    if request.method == 'POST':
        try:
            obj = Author.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'message':'Author deleted successfuly'}, status=status.HTTP_200_OK)
        except(ValueError, KeyError):
            return JsonResponse({'message':'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def author_filter(request, pk):
    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author)
    serializer = BookSerializer(books, many=True)
    filter_books = BookFilter(request.GET, queryset=Book.objects.all())
    context = {
        'qs': serializer.data
    }
    return render(request, 'book_list.html', context)
