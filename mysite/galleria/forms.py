from django import forms
from .models import UserPhoto
from .models import UserGallery

class UploadForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = ['description', 'image', 'galleria', 'tags']

class CreateGalleryForm(forms.ModelForm):
    class Meta:
        model = UserGallery
        fields = ['name', 'private']

#Vanhat:
#class AddPhotoForm(forms.Form):
#   name = forms.CharField(label="Photo name", max_length=250)
   # tähän vois varmaan lisää sen kuvan kans
