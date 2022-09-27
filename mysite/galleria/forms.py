from django import forms
from .models import UserPhoto

class UploadForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = ['description', 'image', 'galleria']

#Vanhat:
#class AddPhotoForm(forms.Form):
#   name = forms.CharField(label="Photo name", max_length=250)
   # tähän vois varmaan lisää sen kuvan kans
