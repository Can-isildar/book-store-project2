"""
URL configuration for bookstore_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', core_views.register, name='signup'),
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    path('homepage/', core_views.home, name='user-home'),
    path('core/',include('core.urls')),
    path('books', include('books.urls'), name='book'),  # books uygulamasının URL'lerini ekleyin
    path('authors/', include('authors.urls'), name='author'),  # authors uygulamasının URL'lerini ekleyin
    path('categories/', include('categories.urls'), name='category'),  # categories uygulamasının URL'lerini ekleyin
    path('publishers/', include('publishers.urls'), name='publisher'),  # publishers uygulamasının URL'lerini ekleyin
    path('cart/', include('cart.urls'), name='cart'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
