from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PublishForm
from .models import Publisher
from .serializers import PublisherSerializer

@login_required
def publisher_list(request):
    form = PublishForm()
    qs = Publisher.objects.all()
    serializer = PublisherSerializer(qs, many=True)
    if request.method == 'POST':
        form = PublishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publishers')
    template_name = 'publisher_list.html'
    context = {'form': form,
               'qs': serializer.data,
               }
    return render(request, template_name, context)


def publisher_update(request, pk):
    obj = Publisher.objects.get(pk=pk)
    form = PublishForm(instance=obj)
    if request.method == 'POST':
        form = PublishForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('publishers')
    template_name = 'update_url.html'
    context = {'form': form,
               'name': 'Publisher',
               }
    return render(request, template_name, context)


def publisher_delete(request, pk):
    obj = Publisher.objects.get(pk=pk)  # uuid kullanılması daha dogru olur artan id yerine kitap sayfa 249
    if request.method == 'POST':
        obj.delete()
        return redirect('publishers')
    template_name = 'delete_url.html'
    context = {'obj': obj,
               'name': 'Publisher',
               }
    return render(request, template_name, context)