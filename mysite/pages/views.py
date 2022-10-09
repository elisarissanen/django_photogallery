from django.shortcuts import render
from galleria.models import UserPhoto

def index(request):
    context = {}
    return render(request, 'pages/index.html', context)


def ITdisplay_images(request):
    if request.method == 'GET':

        queries = UserPhoto.objects.all()

        ITUserPhotos = []
        for x in queries:
            ITUserPhotos.append((x))

        return render(request, 'pages/index.html', {'ITUserPhotos' : ITUserPhotos})
