from email.mime import image
from http.client import HTTPResponse
from multiprocessing import context

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib import messages
from .models import UserGallery
from .models import UserPhoto
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserPhoto
from .forms import UploadForm
from .forms import CreateGalleryForm
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required


def display_images(request, id):
    if request.method == 'GET':
        UserPhotos = UserPhoto.objects.filter(galleria_id=id)
        return render(request, 'galleria/galleria.html',
                      {'UserPhotos': UserPhotos})


def ITdisplay_images(request, tag):
    if request.method == 'GET':
        ITUserPhotos = UserPhoto.objects.filter(tags__name__in=[tag])
        return render(request, 'galleria/tags.html',
                      {'ITUserPhotos': ITUserPhotos})


def display_galleries(request):
    if request.method == 'GET':
        UserGalleries = UserGallery.objects.all()
        return render(request, 'galleria/index.html',
                      {'UserGalleries': UserGalleries})


@login_required
def image_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.owner = request.user
            image.save()
            return redirect('galleria:success')
    else:
        form = UploadForm(request.user)
    return render(request, 'galleria/upload.html', {'form': form})


@login_required
def create_gallery(request):
    if request.method == 'POST':
        formgal = CreateGalleryForm(request.POST)
        if formgal.is_valid():
            obj = formgal.save(commit=False)
            obj.owner = request.user
            obj.save()

            return redirect('galleria:successgal')
    else:
        formgal = CreateGalleryForm()
    return render(request, 'galleria/newgallery.html', {'formgal': formgal})


def success(request):
    return render(request, 'galleria/success.html', {})


def successgal(request):
    return render(request, 'galleria/successgal.html', {})


def index(request):
    return render(request, 'galleria/index.html')


def deleteimage(request, id):
    imageobject = UserPhoto.objects.get(id=id)
    owner = imageobject.owner

    if request.method == "POST" and request.user.is_authenticated and request.user == owner or request.method == "POST" and request.user.is_authenticated and request.user == imageobject.galleria.owner:
        imageobject.delete()
        messages.success(request, "Post successfully deleted!")
        return HttpResponseRedirect("/g/")
    context = {
        'imageobject': imageobject,
        'owner': owner,
    }
    return render(request, 'galleria/deleteimage.html', context)


def deletegallery(request, id):
    galleryobject = UserGallery.objects.get(id=id)
    owner = galleryobject.owner

    if request.method == "POST" and request.user.is_authenticated and request.user == owner:
        galleryobject.delete()
        messages.success(request, "Post successfully deleted!")
        return HttpResponseRedirect("/g/")
    context = {
        'galleryobject': galleryobject,
        'owner': owner,
    }
    return render(request, 'galleria/deletegallery.html', context)


def tags(request):
    UserPhotos = UserPhoto.objects.filter(tags__name=tags)
    return render(request, 'galleria/tags.html', {
        'tags': tags,
        'UserPhotos': UserPhotos
    })


class PhotoCreateView(CreateView):
    model = UserPhoto
    fields = ['name']
    template_name = 'galleria/addphoto.html'
    success_url = reverse_lazy('galleria:index')
