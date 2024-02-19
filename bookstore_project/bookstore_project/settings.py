# settings.py

import os

# Django'nun sağladığı geliştirme ortamı ayarlarını kullanın
from django.conf import settings

# Temel ayarlar
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'your_secret_key'

DEBUG = True

ALLOWED_HOSTS = []

# Yüklenecek uygulamaları belirtin
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'books',  # books uygulamasını ekleyin
    'authors',  # authors uygulamasını ekleyin
    'categories',  # categories uygulamasını ekleyin
    'publishers',  # publishers uygulamasını ekleyin
    'django_filters',
]

# Middleware sırasını belirtin
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'bookstore_project.middleware.custom_authentication.CustomAuthenticationMiddleware',  # Özel kimlik doğrulama middleware'i
]

# URL konfigürasyonu
ROOT_URLCONF = 'bookstore_project.urls'

# Dil ve zaman ayarları
LANGUAGE_CODE = 'tr-TR'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Statik dosyaların konumu
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Şablon dosyalarının konumu
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Veritabanı ayarları
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/homepage/'
LOGOUT_REDIRECT_URL = '/'


# Oturum yönetimi ayarları
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')