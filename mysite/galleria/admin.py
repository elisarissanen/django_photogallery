from django.contrib import admin

# Register your models here.
from .models import User, UserGallery, UserPhoto

# Nää adminit herjaa jotain ja en jaksa selvittää nyt

#class UserAdmin(admin.ModelAdmin):
    #list_display = ('name', 'date')
    #list_filter = ['date']
    #search_fields = ['name']

#class UserPhotoAdmin(admin.ModelAdmin):
    #list_display = ('name', 'created')

admin.site.register(User)
admin.site.register(UserGallery)
admin.site.register(UserPhoto)

#admin.site.register(User, UserAdmin)
#admin.site.register(UserPhoto, UserPhotoAdmin)