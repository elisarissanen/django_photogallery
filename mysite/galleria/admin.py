from django.contrib import admin

# Register your models here.
from .models import User, UserGallery, UserPhoto

# Tää on nyt sit erittäin kökkö ja ei toimi niin kun haluun

#class UserAdmin(admin.ModelAdmin):
    #list_display = ('name', 'created')
    #list_filter = ['name']
    #search_fields = ['name']

admin.site.register(User)
#admin.site.register(UserAdmin)
admin.site.register(UserGallery)
admin.site.register(UserPhoto)