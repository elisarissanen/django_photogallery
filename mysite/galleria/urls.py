from django.urls import path

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

from . import views


app_name = 'galleria'
urlpatterns = [
    path('', display_images, name = 'display_images'),
    path('image_upload', image_upload, name = 'image_upload'),
    path('create_gallery', create_gallery, name = 'create_gallery'),
    path('success', success, name = 'success'),
    path('successgal', successgal, name = 'successgal'),
    path('delete/<int:id>', views.delete, name='delete'),
]
