"""matzip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import matapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', matapp.views.index, name='index'),
    path('blog/', matapp.views.home, name='home'),
    path('blog/create/', matapp.views.create, name='create'),
    path('blog/detail/<int:blog_id>/', matapp.views.detail, name='detail'),
    path('blog/update/<int:blog_id>/', matapp.views.update, name='update'),
    path('blog/delete/<int:blog_id>/', matapp.views.delete, name='delete'),
    path('accounts/', include('allauth.urls')),
    path('login/', matapp.views.login, name='login'),
    path('api/', matapp.views.api, name='api'),
    path('api/1',matapp.views.api1, name='api1'),
    path('api/2',matapp.views.api2, name='api2'),
    path('api/3',matapp.views.api3, name='api3'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
