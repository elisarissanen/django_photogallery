from django import forms

class AddPhotoForm(forms.Form):
    name = forms.CharField(label="Photo name", max_length=250)
    # tähän vois varmaan lisää sen kuvan kans