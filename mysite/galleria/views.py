from http.client import HTTPResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView


from .models import UserGallery

#from .forms import AddPhotoForm
from .models import UserPhoto


from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserPhoto
from .forms import UploadForm
from .forms import CreateGalleryForm

from django.contrib.auth.decorators import login_required

def display_images(request, id):
    if request.method == 'GET':
        UserPhotos = UserPhoto.objects.filter(galleria_id = id)
        return render(request, 'galleria/galleria.html', {'UserPhotos' : UserPhotos})

def display_galleries(request):
    if request.method == 'GET':
            UserGalleries = UserGallery.objects.all()
            return render(request, 'galleria/index.html', {'UserGalleries' : UserGalleries})


@login_required
def image_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('galleria:success')
    else:
        form = UploadForm()
    return render(request, 'galleria/upload.html', {'form' : form})

@login_required
def create_gallery(request):
    if request.method == 'POST':
        formgal = CreateGalleryForm(request.POST)
        if formgal.is_valid():
            formgal.save()
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


def delete(request, id):
  member = UserPhoto.objects.get(id=id)
  member.delete()
  return render(request, 'galleria/index.html', {})

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

