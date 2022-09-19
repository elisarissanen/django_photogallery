from django.db import models

# Create your models here.

class User(models.Model):
    """Database user information"""
    
    # Django luo itse user id:n, alkaa 1, User.objects.get(id=1)
    # Käytetään tätä käyttäjän referointiin?

    date = models.DateTimeField('date created', auto_now_add=True)
    name = models.CharField(max_length=50, default="user") # tää default on aika sos mut testaukseen

    def __str__(self):
        return self.id
    

class UserGallery(models.Model):
    """Database object UserGallery to store images"""
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)



class UserPhoto(models.Model):
    """Single photo with a name, added time, and the photo"""
    usergallery = models.ForeignKey(UserGallery, on_delete=models.CASCADE,blank=True,null=True)
    
    name = models.CharField(max_length=50, default=None) # photo name? joku generointi tähän?
    #img = models.BinaryField(default=None) # save photo as binary object, tähän tarvitsisi lisätä joku default kuva? miten toimii binääri?
    created = models.DateTimeField('date created', auto_now_add=True)
    
    # TAGS, erillinen lista?

    def __str__(self):
        return self.name