from django.db import models

# Create your models here.

class User(models.Model):
    """Kommentti"""
    
    # Django luo itse user id:n, alkaa 1
    # User.objects.get(id=1)

    def __str__(self):
        return self.id
    

class UserGallery(models.Model):
    """Database object UserGallery to store images"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    #def __str__(self):
        #return ??


class UserPhoto(models.Model):
    """Kommentti"""
    usergallery = models.ForeignKey(UserGallery, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=50, default=None) # photo name?
    img = models.BinaryField() # save photo as binary object
    
    # TAGS, erillinen lista?

    def __str__(self):
        return self.name