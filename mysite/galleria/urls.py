from django.urls import path

from . import views

app_name = 'galleria'
urlpatterns = [
    path('', views.index, name='index'),
    #path('add_photo', views.add_photo, name="add_photo")
    path('add_photo', views.PhotoCreateView.as_view(), name='add_photo')
]
