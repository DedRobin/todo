"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from notes.views import index, delete_note, edit_note, logout_view, add_note, register, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('search/', index, name='search'),
    path('delete/', delete_note, name='delete_note'),
    path('edit/', edit_note, name='edit_note'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_note/', add_note, name='add_note'),
    path("api/", include(
        "api.urls", namespace="api"
    )),
]
