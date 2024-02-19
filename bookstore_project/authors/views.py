from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AuthForm
from .models import Author
from .serializers import AuthorSerializer

@login_required
def author_list(request):
    form = AuthForm()
    qs = Author.objects.all()
    serializer = AuthorSerializer(qs, many=True)
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    template_name = 'author_list.html'
    context = {'form': form,
               'qs': serializer.data,
               }
    return render(request, template_name, context)


def author_update(request, pk):
    print('12312312')
    obj = Author.objects.get(pk=pk)
    form = AuthForm(instance=obj)
    if request.method == 'POST':
        print('sadasdads')
        form = AuthForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('authors')
    template_name = 'update_url.html'
    context = {'form': form,
               'name': 'Author',
               }
    return render(request, template_name, context)


def author_delete(request, pk):
    obj = Author.objects.get(pk=pk)  # uuid kullanılması daha dogru olur artan id yerine kitap sayfa 249
    if request.method == 'POST':
        obj.delete()
        return redirect('authors')
    template_name = 'delete_url.html'
    context = {'obj': obj,
               'name': 'Author',
               }
    return render(request, template_name, context)
