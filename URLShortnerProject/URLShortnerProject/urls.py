from django.contrib import admin
from django.urls import path, include
from URLShortnerApp import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('URLShortnerApp.urls')),
]

