from random import paretovariate
from django import forms
from .models import UserPhoto
from .models import UserGallery
from django.db.models import Q

class UploadForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = ['description', 'image', 'galleria', 'tags']
    
    def __init__(self, owner, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['galleria'].queryset = UserGallery.objects.filter(Q(owner = owner) | Q(private = False))
        # ^Tässä tarkistetaan että kuvia lisätessä gallerian valinnassa ei ole mahdollisuutta lisätä kuvaa toisen henkilön private galleriaan

class CreateGalleryForm(forms.ModelForm):
    class Meta:
        model = UserGallery
        fields = ['name', 'private']

#Vanhat:
#class AddPhotoForm(forms.Form):
#   name = forms.CharField(label="Photo name", max_length=250)
   # tähän vois varmaan lisää sen kuvan kans
