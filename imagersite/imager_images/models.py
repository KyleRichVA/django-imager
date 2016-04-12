from __future__ import unicode_literals

from django.db import models
from imager_profile.models import User_Profile

# Create your models here.
PUBLISH_CHOICES = (
        ('PRIV', 'Private'),
        ('SHARE', 'Shared'),
        ('PUBLIC', 'Public'),
    )


class Album(models.Model):
    owner = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    cover = models.OneToOneField('Photo', on_delete=models.SET_DEFAULT,
                                 default=None,
                                 related_name='cover')
    description = models.CharField(max_length=1000)
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    date_published = models.DateField()
    published = models.CharField(max_length=6,
                                 choices=PUBLISH_CHOICES,
                                 default='PUBLIC')


class Photo(models.Model):
    file = models.ImageField(upload_to='photos')
    owner = models.OneToOneField(User_Profile, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.SET_DEFAULT,
                              default=None)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    date_published = models.DateField()
    published = models.CharField(max_length=6,
                                 choices=PUBLISH_CHOICES,
                                 default='PUBLIC')
