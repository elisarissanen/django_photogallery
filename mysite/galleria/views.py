from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import UserPhoto
from .forms import AddPhotoForm

def index(request):
    # context = katsokuvagalleriastakuviajalaitanejärejstykseen
    return render(request, 'galleria/index.html') #, context)

# tähän vois tehdä listview

def add_photo(request):
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
    
    return render(request, 'galleria/addphoto.html', {'form': form})
