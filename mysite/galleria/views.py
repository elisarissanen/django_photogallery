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

#from .forms import AddPhotoForm
from .models import UserPhoto

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserPhoto
from .forms import UploadForm
from .forms import CreateGalleryForm
from django.views.generic import DeleteView

from django.contrib.auth.decorators import login_required

def display_images(request, id):
    if request.method == 'GET':
        UserPhotos = UserPhoto.objects.filter(galleria_id = id)
        return render(request, 'galleria/galleria.html', {'UserPhotos' : UserPhotos})

#def ITdisplay_images(request):
    #if request.method == 'GET':
        #ITUserPhotos = UserPhoto.objects.all()
        #return render(request, 'galleria/tags.html', {'ITUserPhotos' : ITUserPhotos})

# Sama kuin yllä, mutta filtteröi hakusanan mukaan
def ITdisplay_images(request, tag):
    if request.method == 'GET':
        ITUserPhotos = UserPhoto.objects.filter(tags__name__in = [tag])
        return render(request, 'galleria/tags.html', {'ITUserPhotos' : ITUserPhotos})

#def tags_lookup(request):
    # first we get the posted q term, or return 'notfound' if the form fails to provide a value
    #term = request.POST.get('q', 'notfound')
    #return redirect('galleria/tags.html', name = term)


def display_galleries(request):
    if request.method == 'GET':
            UserGalleries = UserGallery.objects.all()
            return render(request, 'galleria/index.html', {'UserGalleries' : UserGalleries})


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
    return render(request, 'galleria/upload.html', {'form' : form})

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
    return render(request, 'galleria/newgallery.html', {'formgal' : formgal})


def success(request):
    return render(request, 'galleria/success.html', {})
    


def successgal(request):
    return render(request, 'galleria/successgal.html', {})



def index(request):
    # context = katsokuvagalleriastakuviajalaitanejärejstykseen
    return render(request, 'galleria/index.html') #, context)


def deleteimage(request, id):
    imageobject = UserPhoto.objects.get(id=id)
    owner = imageobject.owner

    if request.method == "POST" and request.user.is_authenticated and request.user == owner:
        imageobject.delete()
        messages.success(request, "Post successfully deleted!")
        return HttpResponseRedirect("/g/")
    context = {'imageobject': imageobject, 'owner': owner,}
    return render(request, 'galleria/deleteimage.html', context)


def deletegallery(request, id):
    galleryobject = UserGallery.objects.get(id=id)
    owner = galleryobject.owner

    if request.method == "POST" and request.user.is_authenticated and request.user == owner:
        galleryobject.delete()
        messages.success(request, "Post successfully deleted!")
        return HttpResponseRedirect("/g/")
    context = {'galleryobject': galleryobject, 'owner': owner,}
    return render(request, 'galleria/deletegallery.html', context)


def tags(request):
    UserPhotos = UserPhoto.objects.filter(tags__name=tags)
    return render(request, 'galleria/tags.html', {'tags': tags, 'UserPhotos': UserPhotos})


# tähän vois tehdä listview

# Tää toimii ainakin
"""def add_photo(request):
    if request.method == "POST":
        form = AddPhotoForm(request.POST)
        if form.is_valid():
            # TÄMÄHÄN EI NYT TALLENNA MITÄÄN
            # process data
            # message_text = request.POST["message_text"]
            # message = Message(message_text = message_text)
            # UserPhoto.save()
            # Uudelleenohjaus takaisin pääsivulle
            return HttpResponseRedirect(reverse('galleria:index'))
    else:
        form = AddPhotoForm()
    
    return render(request, 'galleria/addphoto.html', {'form': form})"""

# Tää ei toimi mut jätin tähä läpäl
"""@method_decorator(login_required, name='dispatch')
class PhotoCreateView(CreateView):
    model = UserPhoto
    fields = ['name']
    success_url = reverse_lazy('galleria:index')
    form_class = AddPhotoForm
    def form_valid(self, form_class ):
        form_class.instance.user= self.request.user
        return super().form_valid(form)"""

# Sama tän kans
"""@login_required(login_url=reverse_lazy("users:login"))
def profile(request):
profile = Profile.objects.get(user=request.user)
if request.method == "POST":
    form = ProfileUpdateForm(request.POST, instance=profile)
    if form.is_valid():
        form.save(commit = False)
        form.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("users:profile", kwargs="profile")
    
else:
    
    form = ProfileUpdateForm(instance=profile)

context = {"profile":profile,"form":form}

return render(request, "users/profile.html", context)"""

# Tää toimii ehkä tsägäl, paras varmaan jos alottaa tästä ja tekee sit login required
class PhotoCreateView(CreateView):
    model = UserPhoto
    fields = ['name']
    template_name = 'galleria/addphoto.html'
    success_url = reverse_lazy('galleria:index')

