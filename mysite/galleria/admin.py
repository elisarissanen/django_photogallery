from django.contrib import admin
from .models import UserGallery, UserPhoto


class UserGalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'private')

class UserPhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'image', 'pub_date', 'mod_date')
    search_fields = ['description']
    list_filter = ['pub_date', 'mod_date']

admin.site.register(UserGallery, UserGalleryAdmin)
admin.site.register(UserPhoto, UserPhotoAdmin)

