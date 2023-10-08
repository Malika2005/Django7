"""
URL configuration for mylibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from book.views import *


urlpatterns = [
    path('', show_start_page),
    path('showbooks/', show_showbooks_page, name='showbooks'),
    path('showreader/', show_reader_page, name='showreader'),
    path('showrent/', show_rent_page, name='showrent'),
    path('addboоk/', show_addbook, name='addbook'),
    path('addreader/', show_addreader_page, name='addreader'),
    path('addrent/', show_addrent_page, name='addrent'),
    path('showbooks/delete/<int:book_id>', delete_book, name='delete_book'),
    path('showreader/delete/<int:reader_id>', delete_reader, name='delete_reader'),
    path('showrent/delete/<int:rent_id>', delete_rent, name='delete_rent'),
    path('admin/', admin.site.urls),
]
