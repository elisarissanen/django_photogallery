from django.urls import path

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from galleria.views import display_galleries
from .views import *
from galleria.views import display_images
from . import views

app_name = 'galleria'
urlpatterns = [
    path('<int:id>/', display_images, name='display_images'),
    path('tags/<str:tag>', ITdisplay_images,
         name='display_images'),  # iteroitava displöö images
    path('', display_galleries, name='display_galleries'),
    path('image_upload', image_upload, name='image_upload'),
    path('create_gallery', create_gallery, name='create_gallery'),
    path('success', success, name='success'),
    path('successgal', successgal, name='successgal'),
    path('tags', tags, name='tags'),
    path('delete/<int:id>', views.deleteimage, name='deleteimage'),
    path('deletegallery/<int:id>', views.deletegallery, name='deletegallery'),
]
