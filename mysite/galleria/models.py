from django.db import models

# Create your models here.

# TÄTÄ USER MODELIA EI VÄLTTIS KÄYTETÄ
class User(models.Model):
#    """Database user information"""
#
    # Django luo itse user id:n, alkaa 1, User.objects.get(id=1)
    # Käytetään tätä käyttäjän referointiin?

    date = models.DateTimeField('date created', auto_now_add=True)
    name = models.CharField(max_length=50, default="user") # tää default on aika sos mut testaukseen

    def __str__(self):
        return self.name


class UserGallery(models.Model):
    """Database object UserGallery to store images"""
    user = models.OneToOneField(User,
    primary_key=True,
    on_delete=models.CASCADE,
    #help_text=_('User (Required).'),
    )


#def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#    return 'user_{0}/{1}'.format(instance.user.id, filename)



class UserPhoto(models.Model):
    """ kuvan tallennus käyttäjäID:tä vastaavaan sijaintiin media kansiossa """
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)
    """Single photo with a name, added time, and the photo"""
   # usergallery = models.ForeignKey(UserGallery, on_delete=models.CASCADE,blank=True,null=True)
    
    #name = models.CharField(max_length=50, default=None) # photo name? joku generointi tähän?
    #img = models.BinaryField(default=None) # save photo as binary object, tähän tarvitsisi lisätä joku default kuva? miten toimii binääri?
    #created = models.DateTimeField('date created', auto_now_add=True)
    
    # TAGS, erillinen lista?

#    def __str__(self):
#       return self.name
