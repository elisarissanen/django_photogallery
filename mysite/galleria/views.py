from http.client import HTTPResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import AddPhotoForm
from .models import UserPhoto


def index(request):
    # context = katsokuvagalleriastakuviajalaitanejärejstykseen
    return render(request, 'galleria/index.html') #, context)

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

