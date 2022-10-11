from email.policy import default
from unittest.util import _MAX_LENGTH
from urllib import request
from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager


def gallery_owner(instance):
    current_user = request.user
    return '{}'.format(instance.current_user)


class UserGallery(models.Model):
    """Database object UserGallery to store images"""
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User,
                              default=User,
                              on_delete=models.SET_NULL,
                              null=True)
    name = models.CharField(max_length=20)
    private = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)

    def __str__(self):
        return self.name


# Tallennuskansio UserPhotoa ladatessa oikeaan gallerian kansioon
def user_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'gallery_{0}/{1}'.format(instance.galleria.id, filename)


class UserPhoto(models.Model):
    """ kuvan tallennus käyttäjäID:tä vastaavaan sijaintiin media kansiossa """

    galleria = models.ForeignKey(UserGallery,
                                 on_delete=models.CASCADE,
                                 default=0)
    owner = models.ForeignKey(User,
                              default=User,
                              on_delete=models.SET_NULL,
                              null=True)
    image = models.ImageField(upload_to=user_directory_path)
    image_preview = ImageSpecField(source='image',
                                   processors=[ResizeToFill(100, 100)],
                                   format='JPEG',
                                   options={'quality': 60})

    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)
    tags = TaggableManager()

    @property
    def phohtos(self):
        return self.image_preview.all()
