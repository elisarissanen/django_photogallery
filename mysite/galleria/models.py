from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

# TÄTÄ USER MODELIA EI VÄLTTIS KÄYTETÄ
#class User(models.Model):
#    """Database user information"""
#
    # Django luo itse user id:n, alkaa 1, User.objects.get(id=1)
    # Käytetään tätä käyttäjän referointiin?

#    date = models.DateTimeField('date created', auto_now_add=True)
#    name = models.CharField(max_length=50, default="user") # tää default on aika sos mut testaukseen

   # def __str__(self):
   #     return self.name

def gallery_owner(instance):
    current_user = request.user
    return '{}'.format(current.user)

class UserGallery(models.Model):
    """Database object UserGallery to store images"""
    #user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE,#help_text=_('User (Required).'),)
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, default=User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20)
    private = models.BooleanField(default = False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)

    # tää galtsu owner ei nyt tee mitään nyksellää
   # owner2 = gallery_owner(self)

    def __str__(self):
        return self.name


#Tällä autetaan tallennuskansio UserPhotoa ladatessa oikeaan gallerian kansioon
def user_directory_path(instance, filename):
    #file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'gallery_{0}/{1}'.format(instance.galleria.id, filename)



class UserPhoto(models.Model):
    """ kuvan tallennus käyttäjäID:tä vastaavaan sijaintiin media kansiossa """
    #Tähän viittaus tiettyyn galleriaan esim:
    #id = models.AutoField(primary_key=True)
    galleria = models.ForeignKey(UserGallery, on_delete=models.CASCADE, default = 0)
    image = models.ImageField(upload_to=user_directory_path)
    image_preview = ImageSpecField(source='image',
                                  processors=[ResizeToFill(100, 100)],
                                  format='JPEG',
                                  options={'quality': 60})

    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)

   # usergallery = models.ForeignKey(UserGallery, on_delete=models.CASCADE,blank=True,null=True)
    
    #name = models.CharField(max_length=50, default=None) # photo name? joku generointi tähän?
    #img = models.BinaryField(default=None) # save photo as binary object, tähän tarvitsisi lisätä joku default kuva? miten toimii binääri?
    #created = models.DateTimeField('date created', auto_now_add=True)
    
    # TAGS, erillinen lista?

#    def __str__(self):
#       return self.name
