from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'pages'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', views.ITdisplay_images, name = 'ITdisplay_images'),
    path("accounts/", include("django.contrib.auth.urls")),
]
