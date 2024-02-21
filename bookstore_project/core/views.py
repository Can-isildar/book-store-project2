from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Başarılı kayıt olduktan sonra yönlendirme yapılabilir
        else:
            # Form geçerli değilse, hataları görüntüleyin
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


@login_required
def get_profile_detail(request):
    return render(request, 'profile/profile_detail.html')


@login_required
def home(request):
   return render(request, 'core/home.html')


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            print(form.errors)

    else:
        form = UserChangeForm()
    context = {
        'form': form
    }
    return render(request, 'edit_profile.html', context)