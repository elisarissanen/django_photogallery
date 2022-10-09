from django.shortcuts import render
from galleria.models import UserPhoto
import random

def index(request):
    context = {}
    return render(request, 'pages/index.html', context)


def ITdisplay_images(request):
    if request.method == 'GET':
        queries = UserPhoto.objects.all()
        ITUserPhotos = []
        for x in queries:
            if x.galleria.private == False:
                if len(ITUserPhotos) < 10:
                    ITUserPhotos.append(x)
                else:
                    break
        random.shuffle(ITUserPhotos)
        return render(request, 'pages/index.html', {'ITUserPhotos' : ITUserPhotos})
