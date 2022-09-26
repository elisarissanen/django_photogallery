from django.contrib import admin

# Register your models here.
from .models import User
from .models import UserGallery
from .models import UserPhoto

# Nää adminit herjaa jotain ja en jaksa selvittää nyt

#class UserAdmin(admin.ModelAdmin):
    #list_display = ('name', 'date')
    #list_filter = ['date']
    #search_fields = ['name']

#class UserPhotoAdmin(admin.ModelAdmin):
    #list_display = ('name', 'created')


class UserPhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'image', 'pub_date', 'mod_date')
    search_fields = ['description']
    list_filter = ['pub_date', 'mod_date']

admin.site.register(User)
admin.site.register(UserGallery)
admin.site.register(UserPhoto, UserPhotoAdmin)
#admin.site.register(User, UserAdmin)
#admin.site.register(UserPhoto, UserPhotoAdmin)
